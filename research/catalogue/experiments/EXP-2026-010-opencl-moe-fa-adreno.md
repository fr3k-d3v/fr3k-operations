---
id: EXP-2026-010
title: "OpenCL MoE kernels and default flash-attention path on Adreno 840"
related_entry: FBR-2026-001
status: queued
priority: "P2 (31–60 days)"
created_date: 2026-11-28
acceptance_criteria_defined: true
run_started: ""
run_completed: ""
environment: isolated / non-production (required)
---

# Experiment: OpenCL MoE kernels and default flash-attention path on Adreno 840

**Acceptance criteria are defined below, before any run.** Never execute untrusted source code on production infrastructure, data, credentials or networks. Use an isolated test handset or container with no personal accounts.

Source finding: [radar 2026-11-27](../radar/2026-11-27.md), find 2. All upstream performance figures are CLAIM until reproduced here.

## Hypothesis

Label: HYPOTHESIS. With the Adreno E17 workarounds off by default ([PR 33013](https://github.com/ggml-org/llama.cpp/pull/33013)) and the new MoE kernels ([PR 32971](https://github.com/ggml-org/llama.cpp/pull/32971), [PR 33069](https://github.com/ggml-org/llama.cpp/pull/33069)), a small mixture-of-experts GGUF runs on the Adreno 840 via OpenCL faster than on the CPU. No speed figures have been published for these kernels, and PR 33069 targets the Adreno A850 (coverage of the 840 is UNKNOWN).

## Environment

- Hardware: REDMAGIC 11S Pro, stock firmware, test profile only
- Builds: a llama.cpp build at or after PR 33098. Record the exact commit and the OpenCL driver and compiler version.
- Model: a small public MoE GGUF that fits in memory (record the model and hashes).

## Acceptance criteria

1. [ ] The build runs and the log shows which MoE and flash-attention kernels are used on the Adreno 840.
2. [ ] Run with default settings and again with `GGML_OPENCL_ADRENO_E17_QUIRKS=1`. Correctness is checked against the CPU reference on the 20-prompt set.
3. [ ] Prefill and decode tok/s for OpenCL (default), OpenCL (quirks on) and CPU, 3 runs each, coefficient of variation under 10%.
4. [ ] Peak memory and any crash or compiler failure recorded.
5. [ ] Raw logs committed with no device serials or account details.

## Method

Same prompt set and thermal gates as EXP-2026-001. Record negative findings, including any compile failure or wrong output.

## Dependencies

OpenCL only. No Hexagon SDK required.

## Results

Not run.

## Outcome

- Pass / fail against acceptance criteria: not run
