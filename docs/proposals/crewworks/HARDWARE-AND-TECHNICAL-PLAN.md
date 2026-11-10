# 128GB local AI appliance evaluation and engineering plan
Status: Market research 2026-11-11; live quote, freight, stock, GST and benchmark verification pending.

## Candidate classes
1. AMD Ryzen AI Max+ 395 128GB unified LPDDR5X: Minisforum MS-S1 MAX, BOSGAME M5, GMKtec EVO-X2 or comparable. Good x86/Linux application compatibility, lower indicative entry price, CPU/GPU shared memory. Shared memory is NOT 128GB dedicated VRAM; actual model allocation varies by firmware/OS. ROCm/vLLM/llama.cpp support must be proven on exact firmware/kernel/device.
2. NVIDIA DGX Spark / partner GB10 128GB coherent unified memory: NVIDIA AI software ecosystem and CUDA advantage for compatible workloads, ARM64 platform compatibility constraints, higher AU retail price. NOT 128GB discrete VRAM and not necessarily faster for every inference model.
3. Cloud/hybrid fallback: separate app server from inference, allow optional provider API only under data processing/security approval; appliance remains useful if inference is unavailable.

## Observed public listings, NOT binding quotes
- PLE Australia lists MSI EdgeXpert-34SAU 128GB/4TB at A$9,699 and NVIDIA DGX Spark at A$9,999, showing some in-stock locations at research time: https://www.ple.com.au/ai-pc/mini .
- Hypra Tech NVIDIA DGX Spark Founders Edition 128GB/4TB A$10,499 RRP, backorder ETA Feb 2027: https://hypratech.com.au/item/mmt-940-54242-0002-000 .
- Unverified aggregator quotes AMD 128GB machines in roughly A$3k–4.5k range, but currency, region, tax and availability unclear: https://theopstack.com/hardware . Do not represent these as delivered Australian prices.
- NVIDIA manufacturer specs: https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/ .

## Recommended procurement rule
Default AMD 128GB if exact-model benchmark and warranty/availability meet target; select Spark only if CUDA-specific workload benchmark or required framework makes the premium rational. Obtain at least 2 current Australian delivered quotes and vendor return/warranty terms. Avoid buying hardware before contract, acceptance specification and tested inference stack.

## System topology
Private LAN/VPN -> authenticated web app/API -> Postgres authoritative transactions + encrypted evidence object store -> deterministic scheduling/eligibility/rule services -> durable jobs/outbox -> local model gateway with policy enforcement -> optional approved external integrations. No direct model-to-payroll, no default internet exposure. Least privilege, MFA, tenant RBAC, audit, encrypted backups, restore testing, monitored updates and device loss procedure.

## Model workloads and benchmark matrix
Synthetic prompts only: crew FAQ retrieval with citations, roster conflict explanation, 400-person eligibility shortlist, event brief -> quote draft, incident summarisation, EOR document checklist. Compare model size/quantisation, cold start, p50/p95 latency, tokens/s, concurrent requests, memory headroom, CPU/GPU utilization, answer grounding and policy violation rate. Measure idle and peak power, thermals, uptime, recovery from power/network failure. No claim of 200B model usability without workload-specific measured latency.

## Deployment gates
Secure boot/OS support, firmware and driver pinning, supply-chain inventory, isolated services, offline fallback, database restore, encrypted evidence, rate limiting, network hardening, backup restore proof, approval audit, adversarial prompt injection tests, privacy assessment, human acceptance. No unattended hiring or payroll actions.

## Technical build order
Implement synthetic demo first, use existing FR3K Operations #1–#5 prerequisites, add event-production pack from #6, benchmark hardware only after representative workloads exist. Never claim production-ready before end-to-end acceptance.
