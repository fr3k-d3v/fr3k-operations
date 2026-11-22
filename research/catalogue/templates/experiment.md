---
id: YYYY-MM-DD-short-slug
title:
linked_entry:
status: queued
created: YYYY-MM-DD
owner:
---

# Experiment

Copy this file to `experiments/YYYY-MM-DD-short-slug.md`. Add a row to [QUEUE.md](../experiments/QUEUE.md) only after acceptance criteria are written. Templates only; do not invent findings or citations.

This repository is public. Do not record secrets, credentials, tokens, private hostnames, unreleased product internals or other material that should remain private. See [Security and privacy](../../../SECURITY.md).

`status`: queued, running, complete, abandoned. `linked_entry` is the catalogue entry id. Owner is the person accountable for the run.

## Hypothesis

## Acceptance criteria
Must be written and committed before the run. Do not start with this section empty.

## Isolation and safety
Do not run untrusted source code on production infrastructure. Use an isolated virtual machine or container, and review the code before running it.

## Hardware and environment
Platform, accelerator, software versions and isolation boundary. No private hostnames.

## Workload

## Method
Record the methodology so a later reader can repeat it.

## Metrics to record
Performance, thermal behaviour, memory use, cost, quality and failure rate. Record units.

## Results
Leave blank until the run. Label each result. Flag unreproduced results. Unreproduced performance numbers stay CLAIM.

## Negative findings

## Reproducibility details
`reproduced`: yes, no or partial. State what was repeated, on what hardware, and what was not.

## Outcome
Pass or fail against the acceptance criteria. Follow-up. Catalogue updates, including the linked entry's evidence label, confidence and reproduced flag.
