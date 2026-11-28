---
id: EXP-2026-009
title: "OpenCL speculative-decoding verification kernels on Adreno 840"
related_entry: FBR-2026-001
status: queued
priority: "P2 (31–60 days)"
created_date: 2026-11-28
acceptance_criteria_defined: true
run_started: ""
run_completed: ""
environment: isolated / non-production (required)
---

# Experiment: OpenCL speculative-decoding verification kernels on Adreno 840

**Acceptance criteria are defined below, before any run.** Never execute untrusted source code on production infrastructure, data, credentials or networks. Use an isolated test handset or container with no personal accounts.

Source finding: [radar 2026-11-25](../radar/2026-11-25.md), find 1, and [radar 2026-11-27](../radar/2026-11-27.md), find 2. All upstream performance figures are CLAIM until reproduced here.

## Hypothesis

Label: HYPOTHESIS. The batched speculative-decoding verification kernels ([PR 32716](https://github.com/ggml-org/llama.cpp/pull/32716), [PR 32909](https://github.com/ggml-org/llama.cpp/pull/32909), [PR 33098](https://github.com/ggml-org/llama.cpp/pull/33098)) run on the Adreno 840 and raise decode throughput at a fixed acceptance rate. The author figures (27.16 → 32.29, 32.09 → 33.10 and 32.96 → 34.28 tokens/s on a different Adreno) are CLAIM and may not apply.

## Environment

- Hardware: REDMAGIC 11S Pro, stock firmware, test profile only
- Builds: a llama.cpp build before PR 32716 (merged 23 Nov 2026) and a build at or after PR 33098 (merged 27 Nov 2026). Record exact commits.
- Models: one target model and one draft model from the same family, fixed quantisation, hashes recorded.

## Acceptance criteria

1. [ ] Logs show whether each new kernel is selected on the Adreno 840 (the commit notes only mention Snapdragon X2 enablement). A "not enabled" result is a valid outcome and is recorded.
2. [ ] Speculative decoding runs with a fixed draft length and fixed acceptance behaviour (greedy, seed 0). Acceptance rate recorded for every run.
3. [ ] Decode tok/s compared before and after at matched acceptance rate, 3 runs each, coefficient of variation under 10%.
4. [ ] Output identical to the non-speculative greedy output on the 20-prompt set, or any difference flagged.
5. [ ] Raw logs committed with no device serials or account details.

## Method

Use a long prompt (about 32k tokens, matching the author's setup where memory allows) and a short prompt. Report both. Compare against the OpenCL non-speculative baseline from EXP-2026-001.

## Dependencies

Needs only the OpenCL path, so it does not depend on the Hexagon SDK. Share the handset schedule with EXP-2026-001.

## Results

Not run.

## Outcome

- Pass / fail against acceptance criteria: not run
