---
type: weekly-deep-dive
week_starting: 2026-11-16
report_date: 2026-11-22
author: FR3K BLACKSITE RESEARCH
topic: AI-native Android (with "AI as trust layer" add-on)
catalogue_entry: ../entries/2026-11-22-ai-native-android.md
reproduced: false
---

# Deep dive: designing the first AI-native Android

Prepared 22 November 2026, 7:30 PM AEST (Australia/Brisbane). The GitHub dates below are UTC calendar dates, as the GitHub API returns them.

> **Unreproduced results flag.** FR3K has not run any benchmark, build or experiment for this report. Every performance figure is a **CLAIM** by its author or vendor. "Opened" means this research run read the page or repository. Repository star counts and dates were read on 22 Nov 2026 and will change.

## How to read the labels

| Label | Meaning in this report |
|---|---|
| **VERIFIED FACT** | Confirmed from a primary source opened during this run. The link is given. |
| **CLAIM** | Stated by a vendor, author or third party and not reproduced by FR3K. |
| **ASSUMPTION** | Working premise or background knowledge with no source opened this run. Treat it with caution. |
| **HYPOTHESIS** | A testable engineering prediction, linked to an experiment where possible. |
| **UNKNOWN** | Could not be determined from sources available this run. |

---

## 0. Executive answer (one paragraph)

The brief describes Omarchy as an "AI-native Linux". Measured against its own repository in November 2026, that premise largely holds, with one correction. Omarchy is opinionated *integration*: one-command setup, coding agents wired into hotkeys, shared agent instructions and skills, a local-model engine with a curated catalogue, and the OS handing crash dumps to an agent. The model is not built into the kernel. Android can make the same leap, but the analogue is not a ROM full of chatbots. It needs five platform primitives:

1. a shared local inference service (load once, serve many)
2. a typed tool bus (MCP semantics over binder, aligned with Android 16+ AppFunctions)
3. a consent and audit layer
4. NPU-aware scheduling
5. a hardware-rooted trust story

All five can be prototyped today, and prior art already exists (AAOSP, JibarOS, OpenPhone). The recommended path is a no-root userspace build first on the REDMAGIC 11S Pro, then a privileged-service tier, and only then a ROM. On the add-on question: a local model can **advise** on trust, but it cannot **be** the trust root. Hardware keys and verified boot must remain the root. Do not spoof Google attestation.

---

## 1. DISCOVER

### 1.1 What "AI-native" actually means in Omarchy (primary-source check)

Sources opened: the `basecamp/omarchy` repository at default branch `quattro`, HEAD `6b908ce`, committed 2026-11-22 (UTC+01), `version` = `4.0.0.alpha`; the latest release tag `v4.5.0`, published 2026-11-05 UTC. Files read: `manual/17-ai.md`, `docs/local-models.md`, `AGENTS.md` and `README.md`. Repo metadata: created 2025-06-01, about 47.4k stars, MIT licence. https://github.com/basecamp/omarchy

- **VERIFIED FACT:** Omarchy describes itself as "Beautiful, Modern & Opinionated Linux". Its README does not call it AI-native. The AI label is the brief's framing, which these defaults support. [README](https://github.com/basecamp/omarchy)
- **VERIFIED FACT:** It ships launchers for about 24 coding agents without choosing a default. The list includes `claude`, `codex`, `opencode`, `copilot`, `cursor-agent`, `grok`, `qwen`, `pi`, `hermes` and `openclaw`. Most are lazily installed through `mise` on first launch and auto-updated. (`manual/17-ai.md`)
- **VERIFIED FACT:** A default agent is chosen once, through a one-time notification or `omarchy default agent`. It is then bound to a global hotkey (`Super+Shift+Ctrl+A`) and terminal shortcuts. `omarchy agent prompt "..."` launches it straight into a task in the agent's auto-approve mode. (`manual/17-ai.md`)
- **VERIFIED FACT:** Agent instructions and skills are shared. One `~/.agents/AGENTS.md` is symlinked into each harness's own global file (`~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md` and so on). Seven Omarchy skills are symlinked into every harness's skills directory, including `omarchy-diagnose-crash` and `omarchy-make-theme`. (`manual/17-ai.md`)
- **VERIFIED FACT:** The OS hands work to the agent. Omarchy watches `systemd-coredump`, and clicking a "Process crashed" notification passes the core dump to the default agent with a diagnosis skill. This is on by default. (`manual/17-ai.md`)
- **VERIFIED FACT:** It has a local-first model engine. `omarchy-local-ai` is a base package installed on every machine, built from `omacom/omarchy-local-ai` (MIT, created 2026-11-01, 46 stars). It is backed by a curated recipe catalogue that runs models in Podman containers. `omarchy models use best text` picks the best model that fits the machine's RAM and GPU. A top-bar panel shows memory fit and start/stop controls, and `omarchy agent --local` points the default agent at the running model. The manual states: "Your prompts and code stay on the machine." Sources: `manual/17-ai.md`, `docs/local-models.md`, and https://github.com/omacom/omarchy-local-ai
- **VERIFIED FACT:** There is usage and subscription telemetry for the user. An agents panel shows plan limits and usage across Claude, Codex and Grok accounts, with multi-account switching. (`manual/17-ai.md`)
- **VERIFIED FACT:** It is honest about risk. The manual warns that agents launched with `omarchy agent prompt` "run unattended… be ready for them to actually do things". It also says to treat the skills as experimental, use plan mode first, and roll back with `omarchy reinstall configs`. (`manual/17-ai.md`)
- **VERIFIED FACT:** The repo itself is agent-maintained in style. It ships `AGENTS.md` and `CLAUDE.md` at the root with coding conventions for agents. [repo root](https://github.com/basecamp/omarchy)

**Verdict on the premise.** It is **partly VERIFIED and partly CLAIM**. "First AI-native Linux distro" remains a CLAIM: we did not survey every distro, and Omarchy does not use that phrase in its README. Its AI-native character is real, though, and comes from **defaults and integration, not new kernel technology**. The transferable design decisions are:

1. **Opinionated defaults with escape hatches.** It picks for you but never locks you in.
2. **Agent as a first-class OS role.** There is a default agent and a hotkey, much like a default browser.
3. **One source of truth for agent instructions and skills,** fanned out to every harness.
4. **The OS emits events to the agent,** such as crashes and theme changes.
5. **A local-model engine that knows the hardware.** It does fit checks and picks the best model for the machine.
6. **Plain files and CLI everywhere,** so agents can read and change the system.
7. **Explicit risk messaging and rollback.**

### 1.2 State of AI on Android (November 2026)

**Platform (Google)**

- **VERIFIED FACT:** AICore and ML Kit GenAI expose Gemini Nano on-device, including direct prompting and an `AgentRunner` for multi-step tool calling. There are per-app quotas, and **inference is only allowed while the app is the top foreground app.** Calling from a foreground service returns `BACKGROUND_USE_BLOCKED`. Device support is an explicit allow-list (Pixel 9/10/11, Galaxy S25/S26, OnePlus 13/15, many Xiaomi/vivo/OPPO). **No REDMAGIC device is listed.** The page was updated 2026-11-10 UTC. https://developers.google.com/ml-kit/genai
- **VERIFIED FACT:** AppFunctions is an Android 16+ platform API plus a Jetpack library. Google calls it "the mobile equivalent of tools within the Model Context Protocol (MCP)". Apps expose typed functions that agents with `EXECUTE_APP_FUNCTIONS` can discover and execute. It is labelled experimental, and Gemini integration requires the Connected Apps Platform preview. https://developer.android.com/ai/appfunctions
- **VERIFIED FACT:** Android 17 expands AppFunctions and refers to "Android MCP". Google frames Android as moving "from an operating system to an intelligence system". https://developer.android.com/blog/posts/android-17-is-here
- **VERIFIED FACT:** Android Computer Control lets **OEM-preloaded** assistants holding the privileged `ACCESS_COMPUTER_CONTROL` permission run up to six target apps on a background virtual display. They can read screenshots and inject taps and text, behind a system consent dialog, with one session at a time. It is in preview and limited to selected target apps. https://developer.android.com/ai/computer-control
- **CLAIM (third-party book):** Gemini prefers AppFunctions and falls back to Computer Control. The agent loop runs in the Google app (AGSA), and AOSP ships no Computer Control agent. https://aospbooks.github.io/aosp-internal-book/51-ai-appfunctions/
- **VERIFIED FACT:** NNAPI is deprecated, and Google's migration guide points to LiteRT. https://developer.android.com/ndk/guides/neuralnetworks/migration-guide
- **VERIFIED FACT:** LiteRT's `CompiledModel` API supports NPUs from Google Tensor (AOT only, beta), Qualcomm AI Engine Direct/QNN (AOT and on-device), MediaTek NeuroPilot, Samsung Exynos AI LiteCore and Intel OpenVINO. Model and NPU runtime libraries are delivered through Play ("Google Play for On-device AI"). https://developers.google.com/edge/litert/next/npu
- **VERIFIED FACT:** LiteRT's QNN support lists SM8850 (8 Elite Gen 5), SM8750 (8 Elite), SM8650 (8 Gen 3), SM8550 (8 Gen 2), SM8475 and SM8450. https://developers.google.com/edge/litert/next/qualcomm

**Qualcomm stack**

- **VERIFIED FACT:** Nexa AI's `NexaAI/nexa-sdk` repository now redirects to **`qualcomm/GenieX`**. GenieX is BSD-3-Clause, about 8.5k stars, last push 2026-11-20 and marked "developer preview". It describes itself as an on-device GenAI runtime that runs "only on Qualcomm Snapdragon". It brings GGUF models or AI Hub bundles to the Hexagon NPU, Adreno GPU or CPU, and dispatches either to llama.cpp (GGML with Hexagon HTP kernels) or to Qualcomm AI Engine Direct. Android targets are the 8 Elite and 8 Elite Gen 5. https://github.com/qualcomm/GenieX
- **VERIFIED FACT:** An announcement thread in the GenieX repository, dated 21 Mar 2026, says Nexa AI is now a Qualcomm company. https://github.com/qualcomm/GenieX/discussions/1058. **CLAIM:** a co-founder interview says the 12-person team joined in mid-March 2026 and that GenieX dropped non-Qualcomm backends. It also says on-device AI software "is hard to scale" as a standalone business because the real buyer is the OEM. https://www.pingwest.com/a/315521
- **VERIFIED FACT:** Qualcomm AI Hub models and apps are BSD-3-Clause, and both repos were active in Nov 2026: https://github.com/qualcomm/ai-hub-models and https://github.com/qualcomm/ai-hub-apps
- **VERIFIED FACT:** The Snapdragon 8 Elite Gen 5 product brief lists:
  - Hexagon NPU with INT2/INT4/INT8/INT16/FP8/FP16 and "Gen AI model encryption"
  - OpenCL 3.0 and Vulkan 1.3 on Adreno
  - security features: a Trust Management Engine root of trust, Qualcomm TEE, the Qualcomm Type-1 Hypervisor, a **Secure Processing Unit "with support for the Android latest StrongBox software components"**, and "Enhanced AI processing isolation and model protection"

  https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Snapdragon-8-Elite-Gen-5-product-brief.pdf

**Open runtimes**

| Runtime | Android NPU/GPU path | Licence | Status (opened) | Label |
|---|---|---|---|---|
| llama.cpp ([repo](https://github.com/ggml-org/llama.cpp)) | CPU; OpenCL for Adreno 750/810/830/840; **experimental `ggml-hexagon`** backend for HTP v73/v75/v79/v81 | MIT | Hexagon backend merged 2025-10-22 ([PR #16547](https://github.com/ggml-org/llama.cpp/pull/16547)); near-complete op offload ([#18822](https://github.com/ggml-org/llama.cpp/pull/18822)); dynamic mapping past the about 3.5 GB NPU session window, and GGML-HTP coexisting with QNN-HTP ([#21705](https://github.com/ggml-org/llama.cpp/pull/21705), merged 2026-04-10) | VERIFIED FACT |
| LiteRT / LiteRT-LM ([LiteRT](https://github.com/google-ai-edge/LiteRT), [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM)) | NPU through vendor plug-ins, plus GPU and CPU | Apache-2.0 | Active Nov 2026 | VERIFIED FACT |
| GenieX ([repo](https://github.com/qualcomm/GenieX)) | Hexagon, Adreno and CPU; Snapdragon only | BSD-3-Clause | Developer preview | VERIFIED FACT |
| ExecuTorch ([repo](https://github.com/pytorch/executorch)) | QNN backend (`backends/qualcomm`), Vulkan, XNNPACK | BSD (LICENSE file) | Active | VERIFIED FACT |
| MNN ([repo](https://github.com/alibaba/MNN)) | New **Hexagon backend in MNN 3.6.1 (2026-07-22)**, plus GPU and CPU | Apache-2.0 | Active | VERIFIED FACT (per README news) |
| MLC-LLM ([repo](https://github.com/mlc-ai/mlc-llm)) | GPU (OpenCL/Vulkan) through TVM compilation | Apache-2.0 | Active | VERIFIED FACT (repo); NPU path UNKNOWN |
| mllm ([repo](https://github.com/UbiquitousLearning/mllm)) | Mobile multimodal, with QNN work | MIT | Last push 2026-09-30 | VERIFIED FACT (metadata) |
| PowerServe ([repo](https://github.com/powerserve-project/PowerServe)) | NPU-focused serving | Apache-2.0 | **Last push 2025-08-07, likely stale** | VERIFIED FACT (metadata) |
| ONNX Runtime QNN EP ([docs](https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html)) | QNN HTP | UNKNOWN | Docs page live. **`github.com/microsoft/onnxruntime` returned 404 to us on 22 Nov 2026**, cause UNKNOWN | UNKNOWN |
| MediaPipe LLM Inference ([repo](https://github.com/google-ai-edge/mediapipe)) | GPU/CPU | Apache-2.0 | Active. Relationship to LiteRT-LM going forward: ASSUMPTION that LiteRT-LM is the successor path | ASSUMPTION |
| **"Geode"** ([sergqwer/geode](https://github.com/sergqwer/geode)) | Its own engine with NEON, Adreno OpenCL and Hexagon HVX/HMX kernels; NPU+GPU split by default | **AGPL-3.0** | Created 2026-10-30, 4 stars, Android 11+ arm64 | VERIFIED FACT (README). Its benchmarks on a RedMagic 10 Pro (8 Elite) are a **CLAIM** |

**Agents and GUI-automation frameworks** (all opened; metadata as of 22 Nov 2026 UTC)

| Project | What it is | Licence | Created / last push / stars | Runs model on-device? |
|---|---|---|---|---|
| [droidrun → droidrun/mobilerun](https://github.com/droidrun/mobilerun) (repo renamed) | LLM-agnostic mobile agent | MIT | 2025-04-12 / 2026-11-18 / about 10.1k | Host-driven, LLM-agnostic (CLAIM) |
| [X-PLUG/MobileAgent](https://github.com/X-PLUG/MobileAgent) | GUI agent family | MIT | 2024-01-26 / 2026-11-03 / about 9.4k | Typically server models (ASSUMPTION) |
| [TencentQQGYLab/AppAgent](https://github.com/TencentQQGYLab/AppAgent) | Multimodal phone agent | MIT | 2023-12-20 / **2025-03-19 (stale)** / about 6.9k | No (ASSUMPTION) |
| [zai-org/Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM) | AutoGLM-Phone-9B model plus framework | Apache-2.0 | 2025-12-08 / 2026-03-06 / about 26.6k | **No. The README drives the phone over ADB from a host** (VERIFIED FACT) |
| [bytedance/UI-TARS](https://github.com/bytedance/UI-TARS) | GUI-agent model | Apache-2.0 | 2025-01-19 / 2026-01-27 / about 11.7k | Server-scale model (ASSUMPTION) |
| [mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp) | MCP server for driving Android/iOS | Apache-2.0 | 2025-03-28 / 2026-11-18 / about 10.8k | Host-side MCP |
| [minitap-ai/mobile-use](https://github.com/minitap-ai/mobile-use) | Agent using real apps | Apache-2.0 | 2025-08-16 / 2026-11-15 / about 3.4k | Host-side (ASSUMPTION) |
| [RikkaApps/Shizuku](https://github.com/RikkaApps/Shizuku) | ADB/root-level system API access for apps | Apache-2.0 | **Last push 2025-06-18**, so maintenance risk | n/a |

### 1.3 Existing "AI-first Android" OS projects (prior art, all opened)

| Project | Approach | Licence | Dates / stars | Notes |
|---|---|---|---|---|
| [interfaces-inc/OpenPhone](https://github.com/interfaces-inc/OpenPhone) (redirected from `secondly-com/OpenPhone`) | LineageOS 23.2 / Android 16 ROM. Privileged `OpenPhoneAssistant`, framework patches, policy and consent, audit log, heartbeats and watchers. Targets Pixel 9a first | **PolyForm Noncommercial 1.0.0**; commercial use needs a licence (README) | 2026-05-24 / 2026-08-18 / 212 | **VERIFIED FACT:** it calls itself "an AI-native Android OS". Whether the model is local or cloud by default is **UNKNOWN**; the README mentions a "development model broker". **It is the closest competitor to this concept.** |
| [NativoML/AAOSP](https://github.com/NativoML/AAOSP) (archived; was `rufolangus/AAOSP`) | AOSP 15 fork. `<mcp-server>` in the manifest, `LlmManagerService` (llama.cpp in `system_server`, Qwen 2.5 3B), HITL consent and audit, AgenticLauncher | README says Apache-2.0; GitHub shows NOASSERTION | 2026-04-10 / 2026-04-23 / 28 | Cuttlefish-focused (CLAIM via XDA). The design is close to our Tier A |
| [NativoML/JibarOS](https://github.com/NativoML/JibarOS) | Android 16 fork. "AI as a platform primitive": 12 capabilities behind one binder AIDL, shared runtime, KV and memory accounting, OEM-pluggable models | Apache-2.0 | 2026-04-23 / 2026-05-06 / 29 | **CLAIM:** v0.7-rc3 boots on Cuttlefish. No physical device confirmed |
| [Cami-Ose/Anzhi-s-Phone](https://github.com/Cami-Ose/Anzhi-s-Phone) | LineageOS 23.2 on Pixel 6a with an AI "living in the system" | NOASSERTION | 2026-08-23 / 2026-10-06 / 37 | Experimental, source only (VERIFIED FACT, README). Remote-API "brain" per search summary (CLAIM) |

**Key insight (HYPOTHESIS):** the "first AI-native Android" title is contested, so FR3K should not claim "first". OpenPhone and JibarOS/AAOSP already exist. The open gap is **NPU-first, device-specific performance on real Snapdragon hardware** (all three target Pixel or Cuttlefish), plus a **trust and attestation layer that does not depend on Google**.

---

## 2. SOURCE: low-star and recent building blocks (2025–2026)

All rows were opened (README plus GitHub API) on 22 Nov 2026. "arm64" means arm64-v8a mentioned in the README. riscv64 relevance: **none of these projects mention riscv64**. On the platform side, **VERIFIED FACT:** Android riscv64 is still Cuttlefish/emulator-level work tracked in AOSP, with no final NDK ABI noted in the tracking repo as of its 2025Q2 status ([google/android-riscv64](https://github.com/google/android-riscv64)). For this design, riscv64 is a watch item, not a target.

| Project | Purpose | Author | Created / last push (UTC) | Stars | Licence | arm64-v8a | Access model |
|---|---|---|---|---|---|---|---|
| [sergqwer/geode](https://github.com/sergqwer/geode) | Full on-device engine (NEON/OpenCL/HVX/HMX), agent with proot Debian, image and music gen | sergqwer | 2026-10-30 / 2026-11-19 | 4 | AGPL-3.0 | Yes | No root |
| [yuubinnkyoku/HexaTrain](https://github.com/yuubinnkyoku/HexaTrain) | **On-device SLM *training*** on Hexagon v81 (8 Elite Gen 5) through QNN HTP plus HVX | yuubinnkyoku | 2026-07-10 / 2026-11-22 | 3 | Apache-2.0 | Yes | UNKNOWN |
| [Dinesh210805/aura-android-use](https://github.com/Dinesh210805/aura-android-use) | On-device agent plus an MCP server on the phone; accessibility-based | Dinesh210805 | 2026-09-22 / 2026-11-19 | 27 | AGPL-3.0 | UNKNOWN | No root (README) |
| [zephyr7030/DroidBridge](https://github.com/zephyr7030/DroidBridge) | On-device MCP server; Shizuku or accessibility; scheduled automations | zephyr7030 | 2026-09-17 / 2026-11-15 | 26 | Apache-2.0 | Yes (and x86_64) | Shizuku optional |
| [springmusk026/locus](https://github.com/springmusk026/locus) | Local-first agent: BYO model (key, local server or on-device), Linux shell, browser | springmusk026 | 2026-10-31 / 2026-11-21 | 10 | AGPL-3.0 | Yes | No root |
| [Verlintas/NovaBAIC](https://github.com/Verlintas/NovaBAIC) | Local-first agent with 57 device tools and no GMS | Verlintas | 2026-09-28 / 2026-11-11 | 120 | GPL-3.0 | UNKNOWN | Shizuku and accessibility |
| [traveler3022/Hermes-Pocket](https://github.com/traveler3022/Hermes-Pocket) | Nous Hermes Agent running fully on the phone | traveler3022 | 2026-07-01 / 2026-11-13 | 17 | GPL-3.0 | UNKNOWN | No root |
| [gabrielalberton/droidhand](https://github.com/gabrielalberton/droidhand) | Phone control for any AI agent: accessibility plus ADB on demand | gabrielalberton | 2026-11-20 / 2026-11-22 | 0 | Apache-2.0 | UNKNOWN | Accessibility |
| [Anonym0usWork1221/Kelvin](https://github.com/Anonym0usWork1221/Kelvin) | **AI-aware thermal governor** to sustain on-device LLM inference | Anonym0usWork1221 | 2026-07-08 / 2026-07-28 | 10 | MIT | Yes | **Root** |
| [ExperimentalMachines/execupack](https://github.com/ExperimentalMachines/execupack) | Exports Hugging Face LLMs of 4B or less to ExecuTorch `.pte` (XNNPACK/Vulkan/QNN/MediaTek) | ExperimentalMachines | 2026-09-12 / 2026-11-15 | 0 | Apache-2.0 | n/a (export tool) | n/a |
| [mofanx/pilotdroid](https://github.com/mofanx/pilotdroid) | Device-side automation, stdio MCP server (from the description only) | mofanx | 2026-11-19 / 2026-11-22 | 0 | MIT | UNKNOWN | UNKNOWN |
| [GrapheneOS/Auditor](https://github.com/GrapheneOS/Auditor) and [AttestationServer](https://github.com/GrapheneOS/AttestationServer) | Hardware-attestation pairing (TOFU), local or remote | GrapheneOS | 2018 / 2026-11-20 | 731 / 177 | MIT | Yes | No root |
| [android/keyattestation](https://github.com/android/keyattestation) | Kotlin library to evaluate key-attestation chains (replaces the archived `google/android-key-attestation`) | Google (android org) | 2024-09-27 / 2026-11-21 | 159 | Apache-2.0 | n/a (server or JVM) | n/a |

**Licence warning (VERIFIED FACT from the licence fields):** Geode, AURA and Locus are AGPL-3.0, NovaBAIC and Hermes-Pocket are GPL-3.0, and OpenPhone is PolyForm Noncommercial. Use them as **reference designs only** unless FR3K is willing to open-source under the same terms.

---

## 3. REPRODUCE

**Status: nothing reproduced.** No builds, flashes or benchmarks were run. Per the master instructions, nothing from these repos was executed on any FR3K infrastructure. All reproduction is deferred to the experiment queue (section 6), which must run on an isolated test handset with no personal accounts and no FR3K credentials.

## 4. BENCHMARK

No FR3K measurements exist. Published figures noted, all **CLAIM**:

- llama.cpp Hexagon PR #16547 lists models tested up to gpt-oss-20b, "requires latest devices with 16+ GB of DDR". It gives no tok/s in the text we opened. PR #21705 claims support for MoE models up to about 30B in a single HTP session.
- Geode claims measurements on a RedMagic 10 Pro (8 Elite, 16 GB) in Nov 2026: about 0.9 s image encode for Gemma 4, and about 11–12 s for a 512×512 FLUX.2-klein image fully on the NPU (HMX) versus about 94 s on CPU.
- REDMAGIC claims the 11S Pro has "39% enhanced NPU" versus the 10S Pro ([REDMAGIC MEA page](https://mea.redmagic.gg/en/pages/redmagic-11s-pro)).
- LiteRT documentation shows sample NPU compile-cache effects. For example, ResNet-152 initialisation falls from 7,465 ms with NPU compilation to 198 ms with cached compilation, on an unnamed device.

The benchmark plan is in EXP-2026-001.

---

## 5. COMPARE

### 5.1 Linux AI-native versus Android AI-native: what has to change

| Concern | Linux / Omarchy approach | Android reality | What must change for AI-native Android |
|---|---|---|---|
| Install and update | `pacman` plus `mise`, lazy install | APKs in a sandbox, Play delivery, APEX for system modules | Model and runtime packs as **updatable system modules or a shared service app**, not one copy per app. **VERIFIED FACT:** JibarOS cites 300 MB+ of duplication per app as its motivation (CLAIM within its README) |
| Config surface | Plain dotfiles and CLI that agents can edit | Settings DB, per-app private storage, SELinux | A **typed, permissioned tool bus** instead of file editing (AppFunctions or an MCP over binder) |
| Agent identity | Default agent plus hotkey | Assistant role (`ROLE_ASSISTANT`, ASSUMPTION), launcher role; Computer Control is **OEM-preload only** (VERIFIED FACT) | An **agent role** the user chooses, with privileged permissions grantable only to that role-holder |
| Cross-app action | Shell pipes and IPC | Binder, intents; accessibility as the universal fallback | Prefer AppFunctions and binder tools; fall back to accessibility or virtual-display Computer Control with consent |
| Background work | systemd user services | Background execution limits; **AICore blocks background inference** (VERIFIED FACT) | Privileged service exemptions, or a foreground service with a visible notification (ASSUMPTION about policy) |
| Accelerator access | `/dev/dri`, ROCm or CUDA in containers | Vendor HALs and libraries (`libQnnHtp*.so`, FastRPC/cDSP), linker namespaces | An **NPU arbiter**: one owner of HTP sessions and VTCM with a priority queue. **VERIFIED FACT:** llama.cpp made GGML-HTP and QNN-HTP coexist, but VTCM contention is a known issue (#21705) |
| Trust | User owns root; signed packages | Verified boot, key attestation, Play Integrity gating banking, Wallet and DRM | A **hardware-rooted, Google-independent attestation path** for FR3K's own services, keeping Google attestation where third parties demand it (section 8) |
| Observability | journald, coredump hooks | logcat, tombstones, ANR traces | Pipe tombstones and ANRs to the agent like Omarchy's crash hook (needs privileged access: ASSUMPTION) |

### 5.2 Three implementation tiers

**Tier A: ROM / AOSP fork (LineageOS 23.x or GSI based)**

- *Capabilities:*
  - `IntelligenceManagerService` in `system_server`, or better a separate native daemon with a binder interface
  - manifest-declared tools in the AAOSP style, plus AppFunctions compatibility
  - a privileged agent role, Computer Control (we would be the OEM)
  - SELinux domains for the model daemon and direct cDSP/FastRPC access
  - tombstone hooks, and a protected-VM verdict signer if AVF is available
- *Limits:*
  - per-device bring-up and vendor blobs; Qualcomm HTP libraries are proprietary
  - **an unlocked or custom-key bootloader loses Play Integrity DEVICE/STRONG and Google Wallet tap-to-pay** (section 8)
  - GMS licensing is unavailable to a custom ROM (ASSUMPTION)
  - OTA and security-patch burden
- *Effort (ASSUMPTION):* 6–12 person-months for one device to beta, plus at least 0.5 FTE ongoing for monthly security merges.
- *Distribution:* flashable images for enthusiasts, or an OEM partnership.
- *Risks:* bricking, patch lag, legal exposure if vendor blobs are redistributed, and direct competition with OpenPhone and JibarOS.

**Tier B: system app plus privileged service (priv-app, signature permissions, Shizuku or root)**

- *Variants:*
  - **B1:** an OEM or partner preloads us as a priv-app, which gives `MANAGE_VIRTUAL_MACHINE` (preinstalled apps on Android 15+, VERIFIED FACT, [AVF README](https://android.googlesource.com/platform/packages/modules/Virtualization/+/refs/heads/main/libs/framework-virtualization/README.md)), possibly `ACCESS_COMPUTER_CONTROL` (UNKNOWN whether OEM allow-listing is needed) and possibly `EXECUTE_APP_FUNCTIONS` (protection level UNKNOWN)
  - **B2:** Shizuku (ADB-level, no root, but Shizuku itself was last pushed in June 2025)
  - **B3:** Magisk or KernelSU module (root)
- *Capabilities:* B1 gets near-Tier-A ergonomics without forking AOSP. B2 adds input injection, package and appops control, and `pm grant` of development permissions. B3 gives everything, including thermal governors like Kelvin.
- *Limits:* B1 needs an OEM deal. B2 sessions reset on reboot unless wireless debugging is re-enabled (ASSUMPTION). B3 breaks Play Integrity and Wallet like Tier A.
- *Effort (ASSUMPTION):* B2 is about 4–6 person-weeks on top of Tier C. B1 depends on the partner.
- *Distribution:* sideload or GitHub for B2/B3; OEM preload for B1.

**Tier C: userspace only, no root (launcher plus AccessibilityService plus local runtime)**

- *Capabilities:*
  - a home-screen launcher with an agent surface
  - a foreground service hosting the model (llama.cpp with OpenCL and Hexagon, GenieX, or LiteRT-LM)
  - a localhost OpenAI-compatible endpoint plus MCP server
  - an AccessibilityService for screen reading and acting
  - AppFunctions as a *provider* (our own tools) and, where allowed, as a caller
  - hardware-backed attested keys through Android Keystore
- *Limits:*
  - **any running accessibility or screen-capture app triggers Play Integrity's `appAccessRiskVerdict` (`UNKNOWN_CAPTURING` / `UNKNOWN_CONTROLLING`) for apps that opt in**, unless it is a Google-reviewed "verified accessibility service" (VERIFIED FACT, [verdicts](https://developer.android.com/google/play/integrity/verdicts)). Banking apps may therefore refuse to run while the agent is active.
  - Play policy restricts accessibility use (ASSUMPTION; not opened this run)
  - no Computer Control
  - background limits apply
  - AICore is not available on REDMAGIC anyway
- *Effort (ASSUMPTION):* 6–10 person-weeks to a credible MVP on one device.
- *Distribution:* GitHub/F-Droid style sideload at first; Play is possible but accessibility review is a risk.
- *Risks:* fragile UI automation, OEM battery killers (REDMAGIC OS behaviour UNKNOWN), and prompt injection from on-screen content.

**Recommendation:** C, then B2, then A. This is a HYPOTHESIS, to be validated by EXP-001 to EXP-006.

---

## 6. EXPERIMENT: 30/60/90-day queue (acceptance criteria defined up front)

All experiments run on an **isolated test handset** (REDMAGIC 11S Pro plus one Pixel for the attestation baseline). They use no personal Google account and no FR3K production credentials, with public or synthetic data only. Full criteria are in `experiments/EXP-2026-00N-*.md`.

| Window | ID | Experiment | Must-pass acceptance criteria (summary) |
|---|---|---|---|
| 0–30 days | EXP-2026-001 | NPU runtime bake-off on the REDMAGIC 11S Pro: llama.cpp (CPU / OpenCL / Hexagon), GenieX, LiteRT-LM (NPU), MNN (Hexagon) on the same roughly 4B Q4 model | All four produce correct output on a fixed 20-prompt set. Prefill and decode tok/s, joules per token (battery-delta method), peak RAM and 10-minute sustained throughput are recorded three times each. Variance under 10%. Raw logs are committed |
| 0–30 days | EXP-2026-002 | **AI trust layer: minimal no-root verifier** (section 8.6) | See section 8.6. All of criteria 1–8 must pass |
| 0–30 days | EXP-2026-003 | Tier C agent MVP: launcher plus accessibility plus local model with an MCP endpoint | At least 14 of 20 scripted tasks complete with no cloud calls (verified by network capture). Every write action needs on-device confirmation. Audit log present. The Play Integrity `appAccessRiskVerdict` effect is observed with our own test app (or recorded UNKNOWN if a Play-distributed test app is not possible) |
| 31–60 days | EXP-2026-004 | Shared intelligence service: one model process serving at least 3 client apps over bound-service AIDL, with an NPU arbiter | Memory with 3 clients is at most 1.2× a single client. Priority preemption works: a foreground request's p95 latency is under 1.5× its solo latency while a background job runs. No VTCM or HTP session crash across 1 hour |
| 31–60 days | EXP-2026-005 | AppFunctions interop: we act as a provider, then test whether a non-system app can be a caller | Our provider is discoverable through `adb` and Google's test agent. Whether `EXECUTE_APP_FUNCTIONS` is grantable to a sideloaded app is recorded (pass means the answer is determined, either way) |
| 61–90 days | EXP-2026-006 | Measured verdict signing in an AVF protected VM (Pixel first; then the REDMAGIC with `adb shell pm grant … MANAGE_VIRTUAL_MACHINE` if the device supports protected VMs) | The pVM returns an RKP-backed chain with the `1.3.6.1.4.1.11129.2.1.29.1` extension. `codeHash` matches our built payload. An off-device verifier accepts it, and rejects it after a one-byte payload change |
| 61–90 days | EXP-2026-007 | Adversarial evaluation of the local APK-verdict model (prompt injection through manifest, strings and resources) | Corpus of at least 200 benign and at least 200 known-malicious public samples (handled in isolation), plus at least 50 injected variants. False-negative rate on injected variants is at most 1.5× the baseline. No verdict is produced without deterministic static-rule evidence attached |

---

## 7. RECOMMEND

### 7.1 Reference architecture: "FR3K AI-native Android" (working name)

```
┌──────────────────────── User surfaces ────────────────────────┐
│ Agent launcher / overlay · hotkey (side key) · notifications   │
└───────────────▲───────────────────────────────────────────────┘
                │ binder (AIDL) + localhost MCP (dev)            
┌───────────────┴──────── Agent orchestrator ───────────────────┐
│ planner · tool router · consent gate (HITL for writes)         │
│ audit log (append-only, signed with attested key)              │
│ AGENTS.md-style user rules + skills (Omarchy pattern)          │
└───────▲──────────────────────▲─────────────────────▲──────────┘
        │ tools                │ inference           │ trust     
┌───────┴────────┐  ┌──────────┴──────────┐  ┌───────┴──────────┐
│ Tool bus        │  │ Intelligence svc    │  │ Trust service     │
│ AppFunctions ⇄  │  │ load-once-serve-many│  │ Keystore attested │
│ MCP bridge;     │  │ NPU arbiter (HTP    │  │ keys; verdict     │
│ accessibility / │  │ sessions, VTCM);    │  │ signer; optional  │
│ Computer Control│  │ KV-cache pool;      │  │ pVM-measured      │
│ fallback        │  │ model packs         │  │ policy engine     │
└────────────────┘  └─────────┬───────────┘  └──────────────────┘
                              │ llama.cpp(Hexagon/OpenCL) │ GenieX │ LiteRT-LM
                         Hexagon NPU · Adreno GPU · CPU (Snapdragon)
```

Omarchy patterns carried over (HYPOTHESIS that these give the "native" feel):

1. one-command "best model for this phone"
2. a default-agent role with a hardware-key shortcut
3. one rules file and skills shared across agents
4. OS events such as crashes, ANRs and notifications delivered to the agent
5. a memory-fit panel
6. explicit risk messaging plus one-tap rollback

### 7.2 Privacy defaults (proposal)

- Local-first: the cloud is off by default, and each cloud call is shown and logged.
- Per-tool consent for any write. Banking and payment apps are excluded from accessibility actions by default.
- Agent auto-pauses when a sensitive app is foregrounded.
- The audit log stays on the device. Export is explicit.
- No telemetry.

### 7.3 Effort summary (ASSUMPTION; one senior Android engineer plus part-time ML)

| Tier | Effort to credible MVP | Ongoing |
|---|---|---|
| C (no root) | 6–10 person-weeks | Low–medium |
| B2 (Shizuku) | +4–6 person-weeks | Medium (Shizuku maintenance risk) |
| B1 (OEM priv-app) | Partner-dependent | Medium |
| A (ROM) | 6–12 person-months per device | High (monthly security merges) |

---

## 8. AI as Trust Layer: Feasibility, Threat Model, and a Minimal Experiment

### 8.1 How Play Integrity works today

- **VERIFIED FACT:** The verdict JSON has `requestDetails`, `appIntegrity` (`appRecognitionVerdict`: `PLAY_RECOGNIZED`, `UNRECOGNIZED_VERSION` or `UNEVALUATED`), `accountDetails` (`appLicensingVerdict`: `LICENSED`, `UNLICENSED` or `UNEVALUATED`), `deviceIntegrity` and `environmentDetails`. The last holds `appAccessRiskVerdict` and `playProtectVerdict`. Optional `recentDeviceActivity` levels run from LEVEL_1 to LEVEL_4. [verdicts](https://developer.android.com/google/play/integrity/verdicts)
- **VERIFIED FACT:** The device labels are as follows. `MEETS_DEVICE_INTEGRITY` means a genuine, certified device, and on Android 13+ requires hardware-backed proof of a locked bootloader and a certified OEM image. `MEETS_BASIC_INTEGRITY` means the bootloader may be unlocked, and on Android 13+ requires only that the attestation root of trust is provided by Google. `MEETS_STRONG_INTEGRITY` means DEVICE plus security patches within the last year on all partitions (Android 13+). An empty verdict signals hooking, rooting or an emulator. On Android 13+, BASIC and STRONG are returned only when the app is Play-licensed. [verdicts](https://developer.android.com/google/play/integrity/verdicts), [overview](https://developer.android.com/google/play/integrity/overview)
- **VERIFIED FACT, the 2024–2025 change:** announced on 3 Dec 2024 and applied to all integrations in **May 2025**. Verdicts on Android 13+ "require, and make greater use of, hardware-backed security signals using Android Platform Key Attestation". Google says device signals evaluated on its servers fell by about 90% and latency improved by up to about 80% (both CLAIMs). [Android Developers Blog](https://android-developers.googleblog.com/2024/12/making-play-integrity-api-faster-resilient-private.html); enterprise notice: [Android Enterprise community](https://www.androidenterprise.community/service-announcements-37/google-play-integrity-api-behavioral-changes-2114)
- **VERIFIED FACT, the keys:** Android Key Attestation chains must verify to a **Google root**. There are two listed trust anchors, and **a new root began signing chains on 1 February 2026**. Each certificate must be checked against Google's **revocation status list**. **Devices launching with Android 16 support only Remote Key Provisioning (RKP)**, which phases out factory-injected keys. Leaked-key revocations "don't apply to attestation keys certified by the newer RKP mechanism". Google also cautions against verifying on the same device. [key attestation](https://developer.android.com/privacy-and-security/security-key-attestation)
- **What breaks on failure:**
  - **VERIFIED FACT:** Google Wallet tap-to-pay will not run on phones that are rooted, run a custom ROM, have modified factory software or have an unlocked bootloader. [Wallet Help](https://support.google.com/wallet/answer/12200245?hl=en)
  - **CLAIM (community reports, no primary Widevine source opened):** an unlocked bootloader typically drops Widevine from L1 to L3, so streaming services cap at SD. [XDA thread](https://xdaforums.com/t/fix-widevine-l1-unlocked-bootloader.4731374/)
  - **ASSUMPTION:** banking apps and some games that require DEVICE or STRONG will refuse or degrade. Behaviour is app-specific.
- **VERIFIED FACT, terms:** the Play Integrity API Terms of Service (last modified 20 May 2024) forbid using it "to fingerprint or track individual users or devices". They bind *developers using the API*. [terms](https://developer.android.com/google/play/integrity/terms)

### 8.2 Google-independent attestation: existing work (opened)

- **GrapheneOS Auditor and AttestationServer (MIT).** These pair a verifier and the device being checked using hardware-backed keys and **Trust On First Use**. They pin the verified-boot key and detect OS, patch or app downgrades. Verification can be local (Auditor to Auditee by QR code) or scheduled remote. **VERIFIED FACT:** each device model must be explicitly integrated, and the current list is **Pixel 6 to Pixel 10a only**. The REDMAGIC is not supported. [attestation.app/about](https://attestation.app/about)
- **Key-attestation libraries.** `android/keyattestation` (Kotlin, Apache-2.0, active) replaces the archived `google/android-key-attestation`. (VERIFIED FACT, GitHub metadata)
- **FIDO/WebAuthn.** Android's FIDO2 API moved from SafetyNet-based attestation to **hardware-backed `android-key` attestation**, which became the default from early April 2025. (VERIFIED FACT, [Android Developers Blog](https://android-developers.googleblog.com/2024/09/attestation-format-change-for-android-fido2-api.html))
- **AVF, pKVM/Gunyah and Microdroid.** **VERIFIED FACT:** protected VMs can call `AVmPayload_requestAttestation(challenge)` and receive an **RKP-backed certificate chain** plus a private key known only to the pVM. The leaf extension (OID `1.3.6.1.4.1.11129.2.1.29.1`) lists `vmComponents`, each with a `codeHash` and `authorityHash`, so it **measures which payload code is running**. Only Microdroid VMs are supported. [VM remote attestation](https://android.googlesource.com/platform/packages/modules/Virtualization/+/refs/heads/main/docs/vm_remote_attestation.md). **VERIFIED FACT:** AVF APIs are `@SystemApi` behind `MANAGE_VIRTUAL_MACHINE`, which goes to preinstalled apps on Android 15+ and can be granted through `adb shell pm grant` for development. [AVF API README](https://android.googlesource.com/platform/packages/modules/Virtualization/+/refs/heads/main/libs/framework-virtualization/README.md)
- **Confidential computing models.** **VERIFIED FACT (vendor page):** Arm CCA "Realms" (Armv9-A RME) isolate models and data and extend protection to accelerators. [Arm CCA](https://www.arm.com/architecture/security-features/arm-confidential-compute-architecture). Whether CCA is shipped or enabled on any phone SoC is **UNKNOWN**. AMD SEV-SNP and Intel TDX are server-side analogues: **ASSUMPTION**, as no source was opened this run, so they are not cited.
- **Decentralised identity.** **VERIFIED FACT:** W3C Verifiable Credentials Data Model v2.0 became a W3C Recommendation on 15 May 2025 (issuer, holder and verifier model with DID-based subjects). [W3C](https://www.w3.org/TR/vc-data-model-2.0/). **HYPOTHESIS:** a device verdict could be packaged as a VC whose proof key is the attested Keystore key. No academic paper on device DIDs was opened this run, so that literature is UNKNOWN.

### 8.3 A local model as policy engine: feasibility

The proposal is that a small local model reads an APK's manifest, permissions, signing chain and static features, then emits a signed verdict.

- **Security property the signature actually gives (HYPOTHESIS, grounded in the AVF docs above).** A signature from a Keystore key attests only that *something able to use that key on this device* signed the bytes. It does **not** attest which model or runtime produced the verdict, unless signing happens inside a **measured** environment such as a Microdroid pVM, whose `codeHash` covers the model, runtime and policy code. Without that, a compromised app process can sign anything.
- **Failure modes:**
  1. **Compromised model or runtime means compromised trust.** Weights are just data, and swapping them changes verdicts (HYPOTHESIS).
  2. **Prompt injection through APK metadata.** **VERIFIED FACT (paper):** ALIBI (arXiv 2609.19722, Sept 2026) shows that adding non-executed "cover story" text to binaries flipped 30 of 35 baseline-malicious samples to benign on Gemini 2.5 Pro. With a verification-guided defence prompt, 42.9% of malicious samples still reached benign. [arXiv](https://arxiv.org/abs/2609.19722)
  3. **Adversarial evasion.** LLM-assisted adversarial Android samples are an active research area (LAMD, arXiv 2502.13055, seen in search results and not opened in full; treat as CLAIM).
  4. **Non-determinism.** Sampling, quantisation and backend differences between NPU and CPU can change verdicts for the same input (HYPOTHESIS). Mitigate with greedy decoding, a pinned model hash and a fixed backend.
  5. **Small-model weakness** on long, obfuscated inputs (ASSUMPTION).
- **Conclusion:** the model should be an **advisor or classifier whose output is one input to a deterministic policy**. Examples of the deterministic layer: signing-certificate pinning, a permission allow-list, a known-bad hash list. The **trust root must remain hardware keys, verified boot and RKP**. Never let model output alone grant access.

### 8.4 Hybrid design (recommended)

1. **Default, for FR3K-controlled services:** our verifier checks the device's Keystore attestation chain to the Google hardware roots (and the revocation list). It pins the verified-boot key with TOFU, as Auditor does, and accepts a **signed local verdict** about app state. Here the Google root is used purely as *hardware provenance*, which needs no Play Integrity call.
2. **Third-party apps that demand Play Integrity** (banking, Wallet, DRM): leave them on Google's path. This means stock firmware and a locked bootloader on daily-driver devices, and the agent auto-pausing in those apps to avoid `appAccessRisk` flags.
3. **ROM tier:** if FR3K ships a ROM with its own verified-boot key, local attestation still works (`verifiedBootKey` reports our key). Play Integrity DEVICE and STRONG will not, so that tier is for dedicated devices, not daily drivers.

**Legal and ToS (NOT LEGAL ADVICE; get Australian counsel before any product decision):**

- **VERIFIED FACT:** the Play Integrity ToS bind developers who use the API (see section 8.1).
- **Recommendation:** do **not** spoof Google attestation. That rules out leaked keyboxes, PlayIntegrityFix-style modules and attestation-hooking. **ASSUMPTION:** spoofing deceives relying parties (banks, payment networks). It risks breach of contract and terms, possible fraud or misrepresentation exposure, and reputational damage. Leaked keyboxes are routinely revoked anyway (VERIFIED FACT: Google's revocation policy).
- **Simply not using Play Integrity** for our own services carries no ToS issue (ASSUMPTION).
- **VERIFIED FACT (statute):** Australia's *Copyright Act 1968* contains technological-protection-measure circumvention provisions (for example s 116AO). [AustLII](https://www5.austlii.edu.au/au/legis/cth/consol_act/ca1968133/s116ao.html). **ASSUMPTION:** bypassing DRM or attestation-gated access could engage these provisions. Rooting your own device for interoperability is a separate question that needs advice.
- **ASSUMPTION (from a search summary; ACCC page not opened in full):** under the Australian Consumer Law, consumer guarantees survive warranty exclusions, but damage caused by modification may not be covered. [ACCC warranties](https://www.accc.gov.au/consumers/buying-products-and-services/warranties)

### 8.5 REDMAGIC 11S Pro / Snapdragon hardware trust features

| Item | Status | Label |
|---|---|---|
| SoC | **Snapdragon 8 Elite Gen 5 "Leading Version" (SM8850-1-AD)**, 2+6 Oryon V3 up to 4.74 GHz, Adreno 840; Android 16 / Redmagic OS 11.5; 12 GB/256 GB or 16 GB/512 GB | VERIFIED FACT ([REDMAGIC specs](https://redmagic.tech/pages/redmagic-11s-pro-specs), [GSMArena](https://www.gsmarena.com/compare.php3?idPhone1=14669)) |
| Hexagon generation | v81 on 8 Elite Gen 5 (HexaTrain README; llama.cpp targets v81 for 8 Elite Gen 5) | VERIFIED FACT (two consistent sources) |
| Qualcomm TEE, Type-1 hypervisor, SPU with StrongBox components | Listed in Qualcomm's product brief | CLAIM (vendor); **whether REDMAGIC exposes StrongBox to apps is UNKNOWN**, and EXP-002 tests it |
| AVF protected VMs | 8 Elite Gen 5 supports **protected VMs only** (no non-protected VMs) on the Xiaomi 17 Pro | VERIFIED FACT for the Xiaomi 17 Pro (Android Authority, Oct 2025); **REDMAGIC UNKNOWN** |
| QNN/Hexagon inside TEE or pVM | Qualcomm advertises "Enhanced AI processing isolation and model protection" and "Gen AI model encryption" | CLAIM; **no public API for NPU access from a pVM or TEE found: UNKNOWN** |
| Gemini Nano / AICore | Not on Google's supported-device list | VERIFIED FACT (absence, as of 2026-11-10) |
| GrapheneOS Auditor | Not supported (Pixel only) | VERIFIED FACT |
| Bootloader unlock policy for the 11S Pro | Not checked this run | UNKNOWN |

**Path to attested inference on the 11S Pro (HYPOTHESIS):**

- **Step 1 (no root):** a Keystore-attested key signs verdicts. This gives device provenance but not code provenance.
- **Step 2 (developer grant):** the verdict signer, with a CPU-only small model, runs in a Microdroid pVM, which provides code provenance through `vmComponents`. NPU acceleration inside the pVM is **UNKNOWN and likely unavailable** (ASSUMPTION).
- **Step 3:** depends on Qualcomm exposing confidential-NPU APIs. UNKNOWN.

### 8.6 Minimal experiment: EXP-2026-002, "Attested local verdict" (no root)

**Components (all built by FR3K and run on an isolated test device):**

1. **Verifier app (V).** It generates an EC P-256 key in Android Keystore with `setAttestationChallenge(nonce)`, and with `setIsStrongBoxBacked(true)` if available, falling back to TEE. It runs a small local model (for example a roughly 1–3B instruct model through llama.cpp) plus deterministic static rules over a **target APK**: manifest permissions, signing certificate SHA-256 and a set of strings. It emits a JSON verdict containing the APK hash, the signing certificate digest, rule hits, the model ID and hash, the decoding parameters, the model's verdict and a timestamp. It signs the verdict with the attested key.
2. **Off-device verifier (S).** This is a small JVM service on a laptop, never on production infrastructure, using `android/keyattestation`. It checks the chain to Google's hardware roots (both roots), checks the revocation status list, checks the challenge, `attestationSecurityLevel` (TEE or StrongBox), `verifiedBootState` and the app identity (`attestationApplicationId` equals V's package and signing digest), then verifies the verdict signature.
3. **Gate app (G).** A single test app that, before unlocking a dummy feature, sends a fresh challenge to V, receives the verdict and chain, and asks S to verify. It grants access only if S passes **and** the deterministic rules pass **and** the model verdict is "allow".

**Acceptance criteria (defined before running):**

1. On the REDMAGIC 11S Pro and on one Pixel, S validates V's chain to a Google hardware root with `attestationSecurityLevel` of TrustedEnvironment or StrongBox. Record which one, and record StrongBox availability.
2. A replayed verdict with a stale challenge is rejected 10 times out of 10.
3. A verdict modified by one byte is rejected 10 times out of 10.
4. A verdict signed by a software (non-attested) key is rejected 10 times out of 10.
5. The same APK scanned 20 times gives an identical model verdict 20 out of 20 times, with greedy decoding and a pinned model hash.
6. On 10 hand-made APKs with **injected benign-looking cover-story strings** over a malicious permission set, G denies at least 9 of 10 because the deterministic rules veto, regardless of the model.
7. The full round trip (scan, sign, verify) takes under 30 s on the 11S Pro for an APK under 50 MB. This is a CLAIM to measure, not an assumption.
8. No network calls from V other than delivering the verdict to S, confirmed by a packet capture.

**Documented limit:** passing EXP-002 proves *device and key provenance plus tamper-evidence*. It does **not** prove which model produced the verdict. EXP-2026-006 (the pVM) addresses that.

---

## 9. Hardware compatibility matrix

The "NPU LLM path" column refers to open runtimes. All performance figures are unmeasured by FR3K.

| Device / SoC | NPU LLM path (open) | GPU path | AICore / Gemini Nano | AVF | Google-independent attestation (Auditor) | Labels |
|---|---|---|---|---|---|---|
| **REDMAGIC 11S Pro, 8 Elite Gen 5 Leading (SM8850)** | llama.cpp Hexagon v81; GenieX; LiteRT QNN (SM8850 listed); MNN Hexagon | llama.cpp OpenCL (Adreno 840 listed) | **Not supported** | Protected VMs only on 8 Elite Gen 5 (Xiaomi 17 Pro); REDMAGIC UNKNOWN | No; DIY key attestation is possible | VERIFIED FACT / UNKNOWN as noted |
| Snapdragon 8 Elite (SM8750), e.g. RedMagic 10 Pro, Galaxy S25 | llama.cpp Hexagon (v79, ASSUMPTION on mapping); GenieX; LiteRT QNN | OpenCL (Adreno 830 listed) | S25 yes; RedMagic no | Protected only (Z Fold 7 per Android Authority) | No | VERIFIED FACT / ASSUMPTION |
| Snapdragon 8 Gen 3 (SM8650) | llama.cpp Hexagon targets Gen 3; LiteRT QNN | OpenCL (Adreno 750 listed) | Device-dependent | UNKNOWN | No | VERIFIED FACT |
| Snapdragon 8 Gen 2 (SM8550) | llama.cpp HTP v73 (ASSUMPTION on mapping); LiteRT QNN | Adreno 740 not listed: UNKNOWN | Device-dependent | UNKNOWN | No | Mixed |
| Google Tensor G4 (Pixel 9) | LiteRT Google Tensor (AOT, beta) | UNKNOWN | **Yes (Nano 3)** | Non-protected VMs on Tensor G1+ (Linux Terminal) | **Yes (Auditor)** | VERIFIED FACT |
| Google Tensor G5 (Pixel 10) | LiteRT Google Tensor (AOT, beta) | UNKNOWN | **Yes (Nano 4)** | As above | **Yes, with StrongBox** | VERIFIED FACT |
| MediaTek Dimensity 9400 / 9500 | LiteRT MediaTek NeuroPilot (SoC list not opened: UNKNOWN); ExecuTorch MediaTek (execupack) | UNKNOWN | vivo X200/X300 listed (SoC mapping ASSUMPTION) | Non-protected VMs on Dimensity 9400+ | No | Mixed |
| Samsung Exynos 2500 (Z Flip 7) | LiteRT Exynos AI LiteCore | UNKNOWN | Z Flip 7 listed | Non-protected VMs supported | No | VERIFIED FACT |
| Snapdragon 7s Gen 3 (mid-range) | Hexagon via llama.cpp: UNKNOWN (not in targets); LiteRT QNN: not listed | **OpenCL (Adreno 810 listed)** | UNKNOWN | UNKNOWN | No | VERIFIED FACT / UNKNOWN |
| riscv64 Android | None | None | None | n/a | n/a | VERIFIED FACT: platform experimental |

Sources: [llama.cpp OpenCL doc](https://github.com/ggml-org/llama.cpp/blob/master/docs/backend/OPENCL.md), [PR #16547](https://github.com/ggml-org/llama.cpp/pull/16547), [LiteRT QNN](https://developers.google.com/edge/litert/next/qualcomm), [LiteRT NPU](https://developers.google.com/edge/litert/next/npu), [ML Kit GenAI devices](https://developers.google.com/ml-kit/genai), [Android Authority on AVF/Snapdragon](https://www.androidauthority.com/snapdragon-chips-android-linux-terminal-3608648/), [attestation.app](https://attestation.app/about).

---

## 10. Security and privacy implications

- **Agent privilege is the main risk.** An accessibility or Computer Control agent can read and act on everything on screen. Mitigations: per-tool HITL for writes, sensitive-app pause, a signed append-only audit, and no auto-approve mode by default. Omarchy's auto-approve-by-default is acceptable on a dev laptop, not on a phone holding banking and messages (HYPOTHESIS).
- **Indirect prompt injection** from web pages, notifications, messages and APK metadata (ALIBI shows the class is real). Treat all screen and app content as untrusted data. Tool calls need typed schemas and allow-lists.
- **Supply chain:** model weights and runtime binaries must be pinned by hash. The Hexagon SDK and QNN libraries are proprietary, so check their redistribution terms before shipping (UNKNOWN).
- **Play Integrity interaction:** the agent can make banking apps see `UNKNOWN_CONTROLLING`, so build an "agent off" switch per app.
- **Root and ROM tiers lose Wallet and DEVICE/STRONG integrity.** Keep a stock daily-driver device and dedicate test devices.
- **Public repo hygiene:** this report contains no credentials, hostnames or device serials. Keep experiment logs scrubbed of IMEI and serial numbers. Attestation chains include device-unique data, so do not commit raw chains (ASSUMPTION; enforce anyway).

## 11. Commercial angles

Commercial assessment held privately. This public report records no pricing, offers or go-to-market detail.

## 12. Implementation-ready findings for KINGPIN DEV

1. Start Tier C on the REDMAGIC 11S Pro. Use **llama.cpp** (MIT) with `GGML_OPENCL` and the `ggml-hexagon` backend (build with Android NDK plus Hexagon SDK Community Edition; ships `libggml-htp-v81.so`), with **GenieX** (BSD-3) as the comparison. Do not rely on AICore, which is unsupported on REDMAGIC and blocks background inference anyway.
2. Hexagon sessions have an about 3.5 GB virtual window, handled by dynamic mapping since llama.cpp PR #21705. GGML-HTP and QNN-HTP can now share the NPU, but VTCM contention is a known issue. One process should own the NPU (the arbiter).
3. Expose tools twice: as an **MCP server** (localhost, dev) and as **AppFunctions** (Android 16+), so the tool schema is written once.
4. Design for Play Integrity `appAccessRiskVerdict`: auto-pause the AccessibilityService when a banking or payment app is foregrounded.
5. Trust: use `android/keyattestation` (Apache-2.0) off-device. Trust **both** Google roots (a new root signs from 1 Feb 2026) and check the revocation list.
6. Measured signing: prototype Microdroid pVM verdict signing on a Pixel first (`adb shell pm grant <pkg> android.permission.MANAGE_VIRTUAL_MACHINE`), then the REDMAGIC.
7. Licence hygiene: treat AGPL/GPL (Geode, AURA, Locus, NovaBAIC, Hermes-Pocket) and PolyForm-NC (OpenPhone) as read-only reference. Use JibarOS (Apache-2.0) as the architecture reference for a shared binder AI service.

---

## 13. RECORD

- Catalogue entry: `../entries/2026-11-22-ai-native-android.md` (FBR-2026-001)
- Experiments: `../experiments/EXP-2026-001` … `EXP-2026-007`, registered in `../experiments/QUEUE.md`
- Executive summary: `2026-11-22-ai-native-android-exec-summary.md`
- Reproduced: **no**. Unreproduced flag: **set**.

### Could not verify this run (UNKNOWN)

- Why `github.com/microsoft/onnxruntime` returned 404 on 22 Nov 2026
- REDMAGIC 11S Pro: StrongBox exposure, AVF support, bootloader unlock policy, background-kill behaviour
- Any public API for NPU use inside a TEE or pVM on Snapdragon
- Protection level of `EXECUTE_APP_FUNCTIONS` for sideloaded apps
- Whether OpenPhone's default model is local
- Hexagon version mapping for 8 Gen 2 and 8 Elite (assumed v73 and v79)
- Widevine L1 behaviour from a primary source
- Academic literature on device DIDs
- AMD SEV-SNP and Intel TDX details
