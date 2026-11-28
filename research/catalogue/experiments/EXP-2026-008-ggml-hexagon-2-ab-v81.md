---
id: EXP-2026-008
title: "A/B of llama.cpp ggml-hexagon 2.0 on Hexagon v81"
related_entry: FBR-2026-001
status: queued
priority: "P1 (0–30 days)"
created_date: 2026-11-28
acceptance_criteria_defined: true
run_started: ""
run_completed: ""
environment: isolated / non-production (required)
---

# Experiment: A/B of llama.cpp ggml-hexagon 2.0 on Hexagon v81

**Acceptance criteria are defined below, before any run.** Never execute untrusted source code on production infrastructure, data, credentials or networks. Use an isolated test handset or container with no personal accounts.

Source finding: [radar 2026-11-27](../radar/2026-11-27.md), find 1. All upstream performance figures are CLAIM until reproduced here.

## Hypothesis

Label: HYPOTHESIS. The `ggml-hexagon` 2.0 merge ([PR 32582](https://github.com/ggml-org/llama.cpp/pull/32582)) improves prompt processing by at least 20% and token generation by at least 5% on the Hexagon v81 NPU in the REDMAGIC 11S Pro, versus the last build before the merge. The author reports 34–62% and 9–27% on a different v81 phone (CLAIM, not reproduced).

## Environment

- Hardware: REDMAGIC 11S Pro (16 GB), stock firmware, no root, test profile only, charger disconnected for energy runs, 25 °C ambient
- Builds: the last llama.cpp build before the PR 32582 merge (26 Nov 2026, 3:00pm Brisbane) and a build at or after it (for example b12774). Record exact commits.
- Model: Qwen3.5-4B Q4_K_M (the EXP-2026-001 model), plus Q4_0 if the integer matrix-unit mode requires it. Record file hashes.
- Build toolchain: Android NDK plus Hexagon SDK Community Edition, in an isolated build container.

## Acceptance criteria

1. [ ] Both builds load the model and produce coherent output on the EXP-2026-001 20-prompt set (spot-checked against the CPU reference).
2. [ ] Logs prove the Hexagon device opened and layers were offloaded, with no silent CPU fallback.
3. [ ] `llama-bench` pp512 and tg256, 3 runs per build, coefficient of variation under 10%, with the skin and battery temperature gates from EXP-2026-001 enforced.
4. [ ] Prefill and decode deltas reported with mean and standard deviation, and compared with the author's claim.
5. [ ] If the integer matrix-unit mode (`w8a8`) is used, a correctness comparison against the CPU reference is recorded and any divergence is flagged.
6. [ ] Raw logs and build commands committed, with no device serials, hostnames or account details.

## Method

Interleave the two builds (A, B, A, B) to reduce thermal bias. Rest the handset between cells until skin temperature is at or below 40 °C. Record negative findings (crashes, unsupported ops).

## Dependencies

Blocked until the Hexagon SDK is obtained (see [EXP-2026-001](EXP-2026-001-npu-runtime-bakeoff.md)). Runs after the EXP-2026-001 CPU and OpenCL baselines.

## Results

Not run.

## Outcome

- Pass / fail against acceptance criteria: not run
