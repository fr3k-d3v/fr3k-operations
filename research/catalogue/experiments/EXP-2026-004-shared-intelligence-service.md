---
id: EXP-2026-004
title: "Shared intelligence service with NPU arbiter"
related_entry: FBR-2026-001
status: queued
priority: "P2 (31–60 days)"
created_date: 2026-11-22
acceptance_criteria_defined: true
run_started: ""
run_completed: ""
environment: isolated / non-production (required)
---

# Experiment: Shared intelligence service with NPU arbiter

**Acceptance criteria are defined below, before any run.** Never execute untrusted source code on production infrastructure, data, credentials or networks. Use an isolated test handset with no personal accounts.

## Hypothesis

Label: HYPOTHESIS. One model host serving many apps over bound-service AIDL saves memory and keeps foreground latency bounded.

## Environment

- REDMAGIC 11S Pro; 3 FR3K client test apps

## Acceptance criteria

1. [ ] Memory with 3 concurrent clients is at most 1.2x a single client.
2. [ ] Foreground request p95 latency is under 1.5x solo while a background job runs.
3. [ ] No HTP session or VTCM crash across 1 hour of mixed load.
4. [ ] Per-client permission checks enforced (an unauthorised client is rejected).

## Method

Priority queue with preemption at token boundaries; KV-cache pool per client; record memory accounting.

## Results

Not run.

## Outcome

- Pass / fail against acceptance criteria: not run
