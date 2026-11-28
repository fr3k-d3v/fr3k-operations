---
type: watch-log
period: "2026-11-22 to 2026-11-28"
author: FR3K BLACKSITE RESEARCH
subject: "GrapheneOS support for the REDMAGIC 11S Pro"
related_entry: FBR-2026-001
reproduced: false
---

# GrapheneOS and the REDMAGIC 11S Pro: watch log, 22–28 November 2026

A daily check of official GrapheneOS sources for any sign of support for the REDMAGIC 11S Pro. Times are Australia/Brisbane (UTC+10). Evidence labels follow the [catalogue rules](../README.md).

This repository is public. Nothing here records secrets, credentials or private details. See [Security and privacy](../../../SECURITY.md).

## Question

An internal stakeholder stated that GrapheneOS runs on the REDMAGIC 11S Pro (**CLAIM**, not verified). Is there any official support, announced or shipped?

## Baseline, 22 November 2026

Sources: the [supported-devices FAQ](https://grapheneos.org/faq#supported-devices) and the [releases page](https://grapheneos.org/releases). Full detail is in the [Android base comparison](../reports/2026-11-22-android-base-comparison.md).

- **VERIFIED FACT:** official production builds are **Pixel-only**. The list covers the Pixel 6a to the Pixel 10 family, with extended support for the Pixel 6 and 6 Pro. No REDMAGIC, nubia or ZTE device appears.
- **VERIFIED FACT:** on 6 November 2026 the project announced upcoming official support for the **Motorola Signature 27**. No Signature 27 build was listed on 22 November.
- **VERIFIED FACT:** **GrimoireOS** is an *unofficial* GrapheneOS-based port for the REDMAGIC **11 Pro+**, not the 11S Pro. It keeps the OEM vendor, odm, kernel and boot images, and is a distinct OS, not an official GrapheneOS build.
- **UNKNOWN:** whether any private or unofficial build boots on the 11S Pro.

## Daily checks

| Date | Result |
|---|---|
| Sun 22 Nov | Baseline above. |
| Mon 23 Nov | No change reported. |
| Tue 24 Nov | No change reported. |
| Wed 25 Nov | No change reported. |
| Thu 26 Nov | No change reported. |
| Fri 27 Nov | No change reported. |
| Sat 28 Nov | No change. The FAQ device list was re-read and is still Pixel-only. The releases page still shows `2026111800` as the latest release and lists Pixel devices only. |

**OBSERVATION:** the 23–27 Nov rows come from the daily routine's "no change" results. The 28 Nov row was re-read directly while preparing this log. There is no per-day screenshot or saved page copy, so the earlier rows are **not independently re-checkable**.

## Status on 28 November 2026

- **VERIFIED FACT (28 Nov):** official GrapheneOS lists no REDMAGIC 11S Pro support.
- **VERIFIED FACT (as of 22 Nov, not re-checked daily beyond the routine):** Signature 27 announced, no build listed; no 11S Pro port; GrimoireOS targets the 11 Pro+.
- **Recommendation (unchanged):** stay no-root-first on stock firmware, and use a Pixel running GrapheneOS as a hardening and attestation lab. Revisit if the project lists a Snapdragon 8 Elite Gen 5 device or someone publishes a boot log for an 11S Pro.
- **Next review:** the daily routine continues. Escalate on any release note that mentions nubia, ZTE or REDMAGIC.
