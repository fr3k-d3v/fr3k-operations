---
id: EXP-2026-011
title: "llama-quantize target-size fit for handset RAM budgets"
related_entry: FBR-2026-001
status: queued
priority: "P3 (61–90 days)"
created_date: 2026-11-28
acceptance_criteria_defined: true
run_started: ""
run_completed: ""
environment: isolated / non-production (required)
---

# Experiment: llama-quantize target-size fit for handset RAM budgets

**Acceptance criteria are defined below, before any run.** Never execute untrusted source code on production infrastructure, data, credentials or networks. Use an isolated test handset or container with no personal accounts.

Source finding: [radar 2026-11-25](../radar/2026-11-25.md), find 2. All upstream performance figures are CLAIM until reproduced here.

## Hypothesis

Label: HYPOTHESIS. `llama-quantize --target-size` or `--target-bpw` ([PR 15550](https://github.com/ggml-org/llama.cpp/pull/15550)) produces a model that fits a stated RAM budget on the REDMAGIC 11S Pro with perplexity no worse than the nearest standard quant. The author's claim (matched or beat standard quants in 93% of 238 tests) is CLAIM and not reproduced.

## Environment

- Quantisation on a build host in an isolated container; inference on the REDMAGIC 11S Pro test profile
- Build: llama.cpp at or after b12669
- Model: Qwen3.5-4B (or the EXP-2026-001 model) from an unquantised or high-precision source

## Acceptance criteria

1. [ ] Produce a target-size quant and the nearest standard quants (for example Q4_K_M and Q5_K_M) from the same source.
2. [ ] Measure perplexity on a fixed public text sample for each, with the same context length.
3. [ ] Record file size, peak RSS on the handset and decode tok/s for each (3 runs, coefficient of variation under 10%).
4. [ ] State plainly whether the target-size quant matches or beats the standard quant on the sample, and flag that one sample cannot reproduce the 93% claim.
5. [ ] Record the exact command and the calibration data used.

## Method

Run on a single model first. Do not publish conclusions about the 93% claim from one model.

## Dependencies

None. Cheap, so it can run alongside EXP-2026-001 when the handset is free.

## Results

Not run.

## Outcome

- Pass / fail against acceptance criteria: not run
