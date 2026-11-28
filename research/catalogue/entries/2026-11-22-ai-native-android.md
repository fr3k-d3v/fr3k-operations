---
id: FBR-2026-001
title: "AI-native Android: platform design and AI-as-trust-layer feasibility"
discovery_date: 2026-11-22
primary_links:
  - https://github.com/basecamp/omarchy
  - https://developer.android.com/ai/appfunctions
  - https://developer.android.com/ai/computer-control
  - https://developers.google.com/ml-kit/genai
  - https://github.com/ggml-org/llama.cpp/pull/16547
  - https://github.com/qualcomm/GenieX
  - https://developer.android.com/google/play/integrity/verdicts
  - https://developer.android.com/privacy-and-security/security-key-attestation
  - https://android.googlesource.com/platform/packages/modules/Virtualization/+/refs/heads/main/docs/vm_remote_attestation.md
original_source: "FR3K BLACKSITE RESEARCH deep dive, reports/2026-11-22-ai-native-android-deep-dive.md"
author: "Multiple (see report); prior art: interfaces-inc/OpenPhone, NativoML/AAOSP, NativoML/JibarOS"
licence: "Mixed: llama.cpp MIT; LiteRT Apache-2.0; GenieX BSD-3-Clause; Auditor MIT; OpenPhone PolyForm-NC; several agent apps AGPL/GPL"
maintenance_activity: "High for core runtimes (pushes in Nov 2026); prior-art ROMs quiet since May–Aug 2026"
authenticity: VERIFIED FACT (sources opened 2026-11-22); performance figures CLAIM
supported_architectures_hardware: [arm64-v8a, "Snapdragon 8 Elite Gen 5 (REDMAGIC 11S Pro)", "Snapdragon 8 Elite / 8 Gen 3 / 8 Gen 2", "Tensor G4/G5", "Dimensity 9400/9500", "Exynos 2500", "Snapdragon 7s Gen 3 (GPU only, NPU UNKNOWN)"]
dependencies: "Android NDK, Hexagon SDK Community Edition (for ggml-hexagon), QNN/QAIRT libs (proprietary), Android Keystore, optional AVF/Microdroid"
install_complexity: "Tier C medium; Tier B high; Tier A very high"
confidence: medium
reproduced: false
unreproduced_flag: true
claimed_performance: "See report section 4; all CLAIM"
measured_performance: "none"
security_privacy_supply_chain_risk: HIGH (agent privilege, prompt injection, proprietary NPU libs)
fr3k_compatibility: "Good for REDMAGIC 11S Pro on the no-root tier; AICore unavailable on that device"
commercial_relevance: "Commercial assessment held privately"
integration_recommendation: "Tier C no-root MVP first, then Shizuku/privileged, ROM last; AI advises but hardware keys remain trust root"
estimated_integration_cost: "Tier C 6–10 person-weeks (ASSUMPTION)"
status: draft
routing:
  kingpin_dev: true
  money_machine: true
related_experiments: [EXP-2026-001, EXP-2026-002, EXP-2026-003, EXP-2026-004, EXP-2026-005, EXP-2026-006, EXP-2026-007, EXP-2026-008, EXP-2026-009, EXP-2026-010, EXP-2026-011, EXP-2026-012]
last_reviewed: 2026-11-28
---

# AI-native Android: platform design and AI-as-trust-layer feasibility

The full analysis is in [the deep dive](../reports/2026-11-22-ai-native-android-deep-dive.md). A follow-up base comparison (AOSP vs GrapheneOS vs JibarOS, with a LineageOS aside) is in [the base comparison](../reports/2026-11-22-android-base-comparison.md). This entry is the catalogue record.

## Technical summary

- **VERIFIED FACT:** Omarchy's "AI-native" character comes from its defaults:
  - about 24 agent launchers with lazy install, and a default agent bound to a hotkey
  - shared `~/.agents/AGENTS.md` instructions and skills
  - crash dumps handed to the agent
  - a base-installed local-model engine (`omarchy-local-ai`) with hardware fit checks
- **VERIFIED FACT:** Android 16 and 17 add AppFunctions ("Android MCP") and OEM-only Computer Control. AICore/Gemini Nano is allow-listed by device (the REDMAGIC is not listed) and foreground-only.
- **VERIFIED FACT:** llama.cpp has an experimental Hexagon NPU backend (v73–v81). Qualcomm acquired Nexa AI, whose Nexa SDK is now GenieX (BSD-3).
- **Prior art exists (VERIFIED FACT):** OpenPhone (PolyForm-NC ROM), AAOSP (archived) and JibarOS (Apache-2.0, Cuttlefish).
- **HYPOTHESIS:** the FR3K differentiator is NPU-first Snapdragon performance plus a Google-independent trust layer.
- **Base recommendation (22 November 2026):** stay no-root-first on stock REDMAGIC OS. Official GrapheneOS production builds checked that day list Pixels only; the owner claim that GrapheneOS runs on the REDMAGIC 11S Pro could not be verified. Use JibarOS as an architecture reference, GrapheneOS on a Pixel as a hardening and attestation lab, and LineageOS only if a ROM tier is later justified. See the base comparison report.

## Supported architectures and hardware

arm64-v8a only. riscv64 Android is still experimental (VERIFIED FACT, google/android-riscv64). See the matrix in the report, section 9.

## Dependencies and installation complexity

Proprietary Qualcomm libraries (Hexagon SDK, QNN) are needed for NPU paths, and their redistribution terms are UNKNOWN. The Tier A ROM needs per-device vendor blobs.

## Evidence and confidence

- Evidence labels used: VERIFIED FACT, CLAIM, ASSUMPTION, HYPOTHESIS, UNKNOWN
- Confidence level: medium (architecture), unverified (performance)
- Reproduced: no
- Unreproduced results: **flagged** until reproduction is recorded

## Claimed versus measured performance

| Metric | Claimed | Measured | Label | Notes |
|---|---|---|---|---|
| Hexagon backend model size | Up to about 30B MoE in a single HTP session | not measured | CLAIM | llama.cpp PR #21705 |
| FLUX.2-klein 512² on NPU (RedMagic 10 Pro) | about 11–12 s vs about 94 s on CPU | not measured | CLAIM | Geode README |
| 11S Pro NPU uplift vs 10S Pro | 39% | not measured | CLAIM | REDMAGIC marketing |

## Security, privacy and supply-chain risk

- High-privilege agents (accessibility or Computer Control) are a risk in themselves.
- Indirect prompt injection is real. ALIBI (arXiv 2609.19722) flipped 30 of 35 malicious samples to benign.
- Proprietary NPU libraries are a supply-chain concern.
- Running an agent triggers Play Integrity `appAccessRiskVerdict` flags.
- Root and ROM tiers lose Google Wallet and DEVICE/STRONG integrity.
- A local model must not be the trust root.

## Compatibility with FR3K systems

The REDMAGIC 11S Pro (SM8850) is supported by llama.cpp OpenCL and Hexagon, GenieX and LiteRT QNN. AICore is unavailable on it. Its AVF support is UNKNOWN.

## Hardware compatibility matrix

| Hardware / platform | Status | Notes | Label |
|---|---|---|---|
| REDMAGIC 11S Pro (8 Elite Gen 5 Leading, SM8850) | Supported (runtimes) | No AICore; AVF and StrongBox UNKNOWN | VERIFIED FACT / UNKNOWN |
| Pixel 9/10 (Tensor G4/G5) | Supported | AICore yes; Auditor yes | VERIFIED FACT |
| Snapdragon 7s Gen 3 | GPU only | NPU path UNKNOWN | VERIFIED FACT / UNKNOWN |

## Benchmark methodology and results

- Methodology: see EXP-2026-001 (defined, not run)
- Results: none
- Negative findings: none yet
- Reproducibility: n/a

## Commercial relevance

Commercial assessment held privately. Routed to MONEY MACHINE for assessment. Nothing commercial is recorded in this public repository.

## Integration recommendation and estimated cost

- Recommendation: Tier C, then B2, then A. The AI advises on trust; hardware keys and verified boot remain the root. Never spoof Google attestation.
- Estimated integration cost: Tier C MVP 6–10 person-weeks (ASSUMPTION)
- Route to KINGPIN DEV (implementation-ready): yes
- Route to MONEY MACHINE (revenue-relevant): yes

## Follow-up experiments

- [x] Acceptance criteria defined for EXP-2026-001 to EXP-2026-007 (see `../experiments/`)
- [x] Radar follow-ups EXP-2026-008 to EXP-2026-012 added 2026-11-28 (see [QUEUE](../experiments/QUEUE.md))
- EXP-2026-001 is partial: see its Results section
