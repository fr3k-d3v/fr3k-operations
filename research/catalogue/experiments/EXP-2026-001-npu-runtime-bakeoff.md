---
id: EXP-2026-001
title: "NPU runtime bake-off on REDMAGIC 11S Pro"
related_entry: FBR-2026-001
status: partial (blocked on Hexagon SDK and a dedicated test handset)
priority: "P1 (0–30 days)"
created_date: 2026-11-22
acceptance_criteria_defined: true
run_started: 2026-11-22
run_completed: ""
environment: isolated / non-production (required)
---

# Experiment: NPU runtime bake-off on REDMAGIC 11S Pro

**Acceptance criteria are defined below, before any run.** Never execute untrusted source code on production infrastructure, data, credentials or networks. Use an isolated test handset with no personal accounts.

## Hypothesis

Label: HYPOTHESIS. Hexagon-backed runtimes beat OpenCL and CPU for prefill and energy per token on SM8850; decode may be bandwidth-bound and closer.

## Environment

- Hardware: REDMAGIC 11S Pro (16 GB), stock firmware, charger disconnected, 25 °C ambient
- Runtimes (pinned commits or versions recorded; record the Qualcomm AI Runtime version bundled with GenieX, 2.51 or later per [GenieX PR 1698](https://github.com/qualcomm/GenieX/pull/1698)): llama.cpp (CPU / OpenCL / Hexagon), GenieX, LiteRT-LM (NPU), MNN (Hexagon)
- Model: one roughly 4B instruct model in the nearest equivalent quantisation per runtime (record exact files and hashes)

## Acceptance criteria

1. [ ] All runtimes produce coherent output on a fixed 20-prompt public set (spot-checked against a CPU reference).
2. [ ] For each runtime: prefill tok/s, decode tok/s, peak RSS, energy per token (battery-counter delta) and 10-minute sustained decode throughput, each recorded over 3 runs with a coefficient of variation under 10%.
3. [ ] Thermal throttling onset time recorded.
4. [ ] Raw logs and build commands committed, with no device serials or IMEIs.
5. [ ] Safety: no FR3K credentials on the device; public prompts only.

## Method

Same prompts, 512-token prompt and 256-token generation, greedy decoding. Comparison baseline: llama.cpp CPU. Record negative findings (crashes, unsupported ops).

## Results

Partial. Status at 28 November 2026 (Brisbane). No acceptance criterion has been met. All labels below are OBSERVATION from the lab runs, not reproduced elsewhere. Raw run logs are held privately because they contain device and network identifiers.

| Item | Status | Label |
|---|---|---|
| Preflight (22 Nov): OpenCL on the Adreno 840 | Passed. OpenCL 3.0 is available to an unprivileged test profile. | OBSERVATION |
| Preflight: Qualcomm HTP libraries visible to the test profile | Unconfirmed. Reads returned permission denied, so their presence is UNKNOWN. | OBSERVATION |
| Same-day clean CPU baseline (Qwen3.5-4B Q4_K_M, llama.cpp v1.0.0 `b1b770d`, 4 threads) | pp512 58.59 ± 0.31 tokens/s; tg128 14.75 ± 0.17 tokens/s. One session, not repeated on another day. | OBSERVATION |
| Same-day OpenCL baseline (same model, all layers offloaded) | pp512 150.03 ± 23.69 tokens/s; tg128 10.48 ± 0.24 tokens/s. Prefill variance is high. One session. | OBSERVATION |
| GenieX NPU and CPU bench cells (22 Nov) | **Contaminated** by a concurrent large file transfer and a thermal abort. Numbers are not published. Offload to the NPU was not proven in the logs. | OBSERVATION |
| CPU greedy reference set (20 prompts) | First attempt failed (tooling error). A clean rerun on 24 Nov completed 16 of 20 prompts. Two were aborted at a skin-temperature limit and two were not started when the handset dropped off the network. | OBSERVATION |
| GenieX correctness against CPU references | Not scoreable until the reference set is complete. The kill criterion stands: any NPU greedy output that differs from the CPU reference after agreed normalisation fails the NPU cell. | OBSERVATION |
| llama.cpp Hexagon, LiteRT-LM NPU, MNN Hexagon | **Blocked.** The Qualcomm Hexagon SDK and AI Runtime sign-in has not been completed. | OBSERVATION |
| Thermal behaviour | Skin temperature after a single 256-token CPU generation was often 43 to 45 °C, so the 10-minute sustained test needs active rest gating. | OBSERVATION |

Lessons recorded for the rerun: one phase per job with a time cap, host-side energy calculation from raw current and voltage samples (the on-device integer arithmetic overflowed), `--seed 0` on every command, and a lock so no other transfer shares the handset. The first run used a shared handset. The bake-off proper needs a dedicated test handset, as the acceptance criteria require.

## Follow-ups from the radar

- [EXP-2026-008](EXP-2026-008-ggml-hexagon-2-ab-v81.md): A/B of `ggml-hexagon` 2.0 on v81, after the Hexagon SDK is available.
- [EXP-2026-009](EXP-2026-009-opencl-spec-decode-adreno.md): OpenCL speculative-decoding kernels.
- [EXP-2026-010](EXP-2026-010-opencl-moe-fa-adreno.md): OpenCL MoE and flash-attention kernels.
- [EXP-2026-011](EXP-2026-011-quantize-target-size-fit.md): `llama-quantize` target-size fit.

## Outcome

- Pass / fail against acceptance criteria: not complete (see Results)
