---
id: EXP-YYYY-NNN
title: ""
related_entry: ""
status: queued
priority: ""
created_date: YYYY-MM-DD
acceptance_criteria_defined: false
run_started: ""
run_completed: ""
environment: isolated / non-production (required)
---

# Experiment: title

Copy this template to `research/catalogue/experiments/EXP-YYYY-NNN-short-slug.md` and add a row to [QUEUE.md](../experiments/QUEUE.md).

**Acceptance criteria must be defined before the experiment is run.** Do not start a test until `acceptance_criteria_defined` is `true` and the criteria below are complete.

Never execute untrusted source code on production infrastructure, data, credentials or networks. Use isolation and appropriate review.

## Hypothesis

Label: HYPOTHESIS

## Purpose and scope


## Environment

- Isolation method:
- Hardware:
- Software / dependencies (pinned, if known):
- Dataset / workload (synthetic or public only unless authorised):

## Acceptance criteria

Write these first. The experiment passes only if all must-have criteria are met.

1. [ ] Criterion (measurable):
2. [ ] Criterion (measurable):
3. [ ] Safety / isolation criterion:

## Method

- Steps:
- Metrics:
- Comparison baseline:
- What will be recorded (performance, thermal behaviour, memory use, cost, quality, failure rates, negative findings, reproducibility):

## Results

Leave blank until the experiment has been run. Label results as OBSERVATION, EVIDENCE, VERIFIED FACT, SIMULATION or UNKNOWN. Flag anything not reproduced.

## Outcome

- Pass / fail against acceptance criteria:
- Follow-up:
- Catalogue entry updates required:
