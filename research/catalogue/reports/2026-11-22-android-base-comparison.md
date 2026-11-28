---
type: comparison
report_date: 2026-11-22
author: FR3K BLACKSITE RESEARCH
related_entry: FBR-2026-001
topic: Android base comparison for the AI-native Android project (AOSP vs GrapheneOS vs JibarOS; LineageOS aside)
reproduced: false
checked_at: "22 November 2026, evening AEST (Australia/Brisbane)"
---

# Android base comparison: AOSP, GrapheneOS and JibarOS

Prepared 22 November 2026, evening AEST (Australia/Brisbane). This is a targeted add-on to the [AI-native Android deep dive](2026-11-22-ai-native-android-deep-dive.md) (FBR-2026-001). No builds or flashes were run. Effort figures are **ASSUMPTION**.

## Owner claim versus official sources (read this first)

**Owner CLAIM (t8u):** GrapheneOS runs on the REDMAGIC 11S Pro.

**What official GrapheneOS sources said when checked on 22 November 2026 (AEST):** they do **not** list the REDMAGIC 11S Pro, or any nubia, ZTE or REDMAGIC device.

- **VERIFIED FACT:** The official production-support list at [grapheneos.org/faq#supported-devices](https://grapheneos.org/faq#supported-devices) (FAQ section "Which devices are supported?", opened 22 November 2026) is:

  > GrapheneOS has official production support for the following devices:
  > Pixel 10a (stallion), Pixel 10 Pro Fold (rango), Pixel 10 Pro XL (mustang), Pixel 10 Pro (blazer), Pixel 10 (frankel), Pixel 9a (tegu), Pixel 9 Pro Fold (comet), Pixel 9 Pro XL (komodo), Pixel 9 Pro (caiman), Pixel 9 (tokay), Pixel 8a (akita), Pixel 8 Pro (husky), Pixel 8 (shiba), Pixel Fold (felix), Pixel Tablet (tangorpro), Pixel 7a (lynx), Pixel 7 Pro (cheetah), Pixel 7 (panther), Pixel 6a (bluejay).
  >
  > GrapheneOS provides extended support for end-of-life for the following devices: Pixel 6 Pro (raven), Pixel 6 (oriole).

  The same FAQ says other devices are supported *at a source level* (AOSP device trees can be dropped in), but "in most cases, substantial work beyond that will be needed" and "for most devices, the hardware and firmware will prevent providing a reasonably secure device". It also says GrapheneOS is **not** supported as a Generic System Image.

- **VERIFIED FACT:** [grapheneos.org/releases](https://grapheneos.org/releases) (opened the same day) publishes official builds only for those same Pixel models. The current Stable/Beta/Alpha version shown was `2026111800`. There is no REDMAGIC, nubia, ZTE or Motorola section on that page.

- **VERIFIED FACT:** GrapheneOS is **no longer a Pixel-only project as a matter of policy**, but official production builds on 22 November 2026 were still Pixel-only. On 6 November 2026 the project account announced **upcoming official support** for the **Motorola Signature 27** as "the first Motorola device supported by GrapheneOS". That post is at [grapheneos.social/@GrapheneOS/117570913006181046](https://grapheneos.social/@GrapheneOS/117570913006181046). The Signature 27 was **not** on the FAQ production list or the releases page when those pages were opened.

- **VERIFIED FACT (unofficial port, different model):** [moexland/mdevtool](https://github.com/moexland/mdevtool) (MIT, created 4 November 2026, last push 6 November 2026, 0 stars) and [moexland/local_manifests](https://github.com/moexland/local_manifests) describe **GrimoireOS**, "a port of GrapheneOS to the nubia RedMagic 11 Pro+ (NX809J)". The local-manifest README says the system comes from GrapheneOS tag `2026110200`, while vendor, odm, kernel and boot images are kept from stock `RedMagicOS11.0.23MR1`. That is the **11 Pro+**, not the **11S Pro**, and it is a **distinct OS based on GrapheneOS**, not an official GrapheneOS build. GrapheneOS's trademark FAQ requires forks that change more than the update-server URL to use their own name and branding ([grapheneos.org/faq](https://grapheneos.org/faq), "What about the GrapheneOS name and logo?").

**Conclusion for this matrix:** the owner's REDMAGIC 11S Pro claim is recorded as an **owner CLAIM that could not be verified** from official GrapheneOS sources on 22 November 2026. This report therefore does **not** state "Pixel-only" as an unconditional fact, and it does **not** treat official GrapheneOS as a ready base for the 11S Pro. If the owner has a private or unofficial build that boots on the 11S Pro, that should be verified separately (device codename, boot log, verified-boot key, and whether Hexagon libraries are present).

---

## Licence and trademark

| Base | Licence and redistribution | Label |
|---|---|---|
| **AOSP** | Preferred licence is Apache License 2.0 for userspace. The Linux kernel is GPLv2 (with system exceptions). [AOSP licences](https://source.android.com/docs/setup/about/licenses) | VERIFIED FACT |
| **GrapheneOS** | GrapheneOS's own standalone code is published under the MIT licence at [grapheneos.org/LICENSE.txt](https://grapheneos.org/LICENSE.txt) (copyright 2014–2026). The FAQ says upstream licences are inherited for modifications, and MIT is used for standalone GrapheneOS projects. Commercial use, modification, distribution and sale are permitted if the copyright and permission notices are kept. **The GrapheneOS name and logo are trademarks**, registered in the United States (serial numbers 90746220 and 90746226) and stated to be in the process of Canadian registration, with common-law protection in the meantime. Forks that are published or redistributed **must replace GrapheneOS branding**. Only a rebuild of the official sources with a changed update-server URL may be called an unofficial GrapheneOS build. [FAQ](https://grapheneos.org/faq) | VERIFIED FACT |
| **JibarOS** | Apache License 2.0. Confirmed from the licence file in [NativoML/JibarOS](https://github.com/NativoML/JibarOS) (opened earlier today). | VERIFIED FACT |
| **LineageOS** (aside) | Android contributions are expected to be Apache 2.0; kernels must be GPLv2. [LineageOS charter](https://github.com/LineageOS/charter/blob/main/device-support-requirements.md); [vendor_lineage LICENSE](https://github.com/LineageOS/android_vendor_lineage/blob/lineage-21.0/LICENSE) | VERIFIED FACT |

---

## Comparison matrix

| Criterion | Plain AOSP | GrapheneOS | JibarOS | LineageOS (aside) |
|---|---|---|---|---|
| **Licence status** | Apache 2.0 userspace, GPLv2 kernel | MIT for GrapheneOS-owned standalone code; inherited upstream licences; **trademark on the name and logo** — a FR3K fork must be rebranded | Apache 2.0 | Apache 2.0 userspace, GPLv2 kernel |
| **Official device support (22 Nov 2026)** | No shipping phone images in the old "AOSP supports Pixel" sense. GrapheneOS states that Android 16 dropped Pixel support from AOSP, and that Pixels now need reverse engineering ([GrapheneOS, 6 Nov 2026](https://grapheneos.social/@GrapheneOS/117570913006181046)). Typical targets are Cuttlefish / emulator. | Official production builds: **Pixels listed above only**. Upcoming official support announced for **Motorola Signature 27** (Snapdragon), not yet on the releases page. **REDMAGIC 11S Pro is not listed.** Unofficial GrimoireOS targets RedMagic **11 Pro+** (NX809J), not 11S Pro. | **Cuttlefish / emulator only** so far (CLAIM from the project's own README and v0.7-rc3 note, opened in the deep dive; no physical device was confirmed) | Broad official device list, including many Snapdragons, on a weekly buildbot ([LineageOS/android](https://github.com/LineageOS/android/)). Whether the 11S Pro itself has an official LineageOS build is **UNKNOWN** this run |
| **Maintenance burden** | Follow AOSP / Android security bulletins and quarterly platform releases. Device bring-up (kernel, vendor HALs, firmware, SELinux) is entirely on FR3K. Google's public ASB cadence has become less complete (CLAIM via LineageOS Changelog 30, Oct 2025). | Fast official cadence: multiple tagged releases in November 2026, current `2026111800` on the Pixel channels. The cost of a *fork* is merging that stream plus device trees. An unofficial Snapdragon port must also track OEM firmware. Trademark requires a new name. | Last GitHub push seen earlier today: **6 May 2026** (29 stars). Rebase onto current AOSP 16/17 would be a large catch-up. | Weekly official images for supported devices; security patches follow public AOSP bulletins, which LineageOS has said are now lumpier |
| **SELinux / hardening defaults** | Stock AOSP SELinux, verified boot if the device tree enables it, standard app sandbox | **Hardened** SELinux and seccomp-bpf, improved app sandbox, signed kernel modules, and other hardening beyond AOSP 16 ([features](https://grapheneos.org/features)). Hardware-backed features (USB-C port control, MTE and so on) are **device-specific** | AOSP 16 baseline plus whatever the fork added for its AI service. Extra GrapheneOS-style hardening is **UNKNOWN** (not claimed in the README opened earlier) | Stock-like AOSP SELinux with device-maintainer policy. Hardening is weaker than GrapheneOS (**ASSUMPTION**, widely reported; not re-audited this run) |
| **Play Services** | None in AOSP. GMS is a separate, licensed Google package and is not available to a typical custom ROM (**ASSUMPTION** on current GMS licensing; not re-opened this run) | **None by default.** Optional **sandboxed Google Play**: official Play Store, Play services and GSF installed as ordinary unprivileged apps, no special SELinux domain or system privileges, per user profile ([features](https://grapheneos.org/features)) | None (the README positions itself against AICore / Google-served models) | None by default. Community "GApps" packages exist; they are not sandboxed like GrapheneOS (**ASSUMPTION**) |
| **NPU / Hexagon accessibility** | On a Snapdragon tree, Hexagon access is through **Qualcomm vendor blobs** (`libQnnHtp*.so`, FastRPC, firmware) in the vendor image. AOSP itself does not ship those. On Pixel, the path is **Google Tensor**, via LiteRT's Tensor backend (AOT, beta) — not Hexagon | **On official Pixels:** Tensor, not Hexagon. AICore / Gemini Nano is a privileged Google component and is **not** expected to ship with GrapheneOS (**HYPOTHESIS**; AICore was also not on the REDMAGIC allow-list in the deep dive). LiteRT Tensor may still be usable if the Tensor runtime libraries are present in the device tree — **UNKNOWN**. **If GrapheneOS, or a GrapheneOS-based port, runs on Snapdragon:** see the section below | No device NPU path demonstrated. Cuttlefish is CPU (and maybe virtual GPU). Snapdragon Hexagon would need a real device tree and vendor blobs | Practical Snapdragon ROM base: maintainers already import OEM vendor blobs. That is the usual way to get `libQnnHtp` and friends onto a custom system image. Redistribution terms for those blobs remain **UNKNOWN** |
| **MCP / AppFunctions compatibility** | AppFunctions is an Android 16+ platform API, so a current AOSP 16/17 tree should contain it unless stripped. Computer Control is OEM-preload only | Almost certainly present as part of the AOSP 16 base (**ASSUMPTION** — GrapheneOS forks `platform_frameworks_base`, so stripping is possible and was not checked). Sandboxed Play does **not** give the privileged `ACCESS_COMPUTER_CONTROL` path | JibarOS already has a **binder AIDL "OpenIntelligence" service** (12 capabilities, load-once-serve-many). That is closer to the desired intelligence service than stock AppFunctions. AppFunctions may also exist as AOSP 16 API (**ASSUMPTION**) | Android 16-based LineageOS 23.x should include AppFunctions unless stripped (**ASSUMPTION**). OpenPhone (a LineageOS 23.2 ROM) already built a privileged agent on this base |
| **Estimated effort to add a local model service + agent** | **ASSUMPTION:** 6–12 person-months for one real device, because device bring-up dominates, then 6–10 person-weeks for a userspace agent on top if the image already boots | **ASSUMPTION:** on an official Pixel, 8–16 person-weeks for a privileged service that respects GrapheneOS sandboxing, plus ongoing merge cost. As a base for the **11S Pro**, official GrapheneOS is not a starting point until official or verified unofficial support exists. An unofficial Snapdragon port (rebranded) is **6–12+ person-months** (merge GrapheneOS + OEM firmware + SELinux for cDSP) | **ASSUMPTION:** the AI service is the valuable part; the device base is not. Porting JibarOS to a phone is AOSP device bring-up plus a 7-month rebase (last push May 2026): **6–12 person-months**. Extracting the binder service as a reference implementation is **days to a few weeks** | **ASSUMPTION:** lowest ROM-path effort for Snapdragon if a device tree exists or can be derived: **4–8 person-months** to a privileged agent on one device, lower if a community tree already boots. Matches the OpenPhone precedent |

---

## If GrapheneOS (or a GrapheneOS-based port) runs on Snapdragon: what changes for NPU / Hexagon

This section is written so the hardware path is clear **if** the owner's claim is later verified, or if FR3K uses official GrapheneOS on the Motorola Signature 27 once builds exist, or studies the unofficial GrimoireOS 11 Pro+ work.

- **VERIFIED FACT:** Official GrapheneOS Pixels are Tensor devices. Hexagon / QNN is a Qualcomm path and is not how official Pixel builds reach an NPU.
- **HYPOTHESIS, with supporting evidence from GrimoireOS:** a GrapheneOS-based Snapdragon port would almost certainly keep the OEM **vendor / odm / firmware** image, as GrimoireOS does for the 11 Pro+. Qualcomm HTP libraries and FastRPC usually live there. Open runtimes from the deep dive (llama.cpp `ggml-hexagon`, GenieX, LiteRT QNN, MNN Hexagon) could then load those libraries, subject to linker namespaces and SELinux.
- **HYPOTHESIS:** GrapheneOS's tighter SELinux and seccomp policy will need **explicit allow rules** for the Hexagon daemon, FastRPC and ION/DMA-buf mappings. That is extra policy work, not a free gift of the port.
- **VERIFIED FACT:** LiteRT's Play-delivered NPU runtime packs ("Google Play for On-device AI") assume Play distribution. Sandboxed Play may or may not deliver those packs — **UNKNOWN**. Do not depend on them; ship or sideload the runtime with the app or privileged service.
- **VERIFIED FACT (GrapheneOS, October 2025, discussion forum):** the project said Snapdragon 8 Elite Gen 5 implements MTE, but they did not yet know if it works well. A later August 2026 post said 8 Elite Gen 5 shipped MTE, "but it's broken on the non-Elite SoC". Whether MTE is usable on the 11S Pro (SM8850 Leading Version) is **UNKNOWN**.
- **VERIFIED FACT:** GrapheneOS Auditor officially supports **Pixels only** (deep dive). A Snapdragon GrapheneOS or GrimoireOS build would need its verified-boot key added before Auditor-style checks work.
- **Play Integrity:** a custom verified-boot key will not produce `MEETS_DEVICE_INTEGRITY` / `MEETS_STRONG_INTEGRITY` on Android 13+ (**ASSUMPTION** grounded in Google's verdict definitions from the deep dive). That is the same Wallet / banking trade-off already recorded for any ROM tier.

---

## Recommendation

Stay with the deep dive's **no-root-first** path. None of these three bases is required for a Tier C launcher, local runtime and accessibility agent on the stock REDMAGIC 11S Pro, and a custom ROM still costs Play Integrity DEVICE/STRONG and Google Wallet tap-to-pay.

Do **not** treat official GrapheneOS as the 11S Pro starting point. Its official production list, checked today, is Pixel-only; Motorola Signature 27 support is announced but not shipping; and the only GrapheneOS-based RedMagic work found is unofficial **GrimoireOS on the 11 Pro+**, which must not be branded as GrapheneOS.

Use the three projects as **references and secondary devices**, not as the first implementation base: JibarOS (Apache 2.0) for the shared binder intelligence service; GrapheneOS for hardening, sandboxed Play, and attestation lab work on a **Pixel**; LineageOS 23.x as the practical Snapdragon ROM base **if and when** a ROM tier is justified (OpenPhone already took that path). A FR3K ROM must use its own name.

---

## Sources opened for this add-on

- [grapheneos.org/faq](https://grapheneos.org/faq) (device list, licensing, trademark), 22 November 2026
- [grapheneos.org/LICENSE.txt](https://grapheneos.org/LICENSE.txt)
- [grapheneos.org/releases](https://grapheneos.org/releases), 22 November 2026
- [grapheneos.org/features](https://grapheneos.org/features) (sandbox, sandboxed Play)
- [grapheneos.org/build](https://grapheneos.org/build) (build targets, all Pixel)
- [GrapheneOS Mastodon, 6 November 2026](https://grapheneos.social/@GrapheneOS/117570913006181046) (Motorola Signature 27 upcoming support)
- [moexland/mdevtool](https://github.com/moexland/mdevtool) and [moexland/local_manifests](https://github.com/moexland/local_manifests) (GrimoireOS, RedMagic 11 Pro+)
- [AOSP licences](https://source.android.com/docs/setup/about/licenses)
- [NativoML/JibarOS](https://github.com/NativoML/JibarOS) (from the deep dive, re-checked licence file)
- [LineageOS charter licensing](https://github.com/LineageOS/charter/blob/main/device-support-requirements.md)

## Unverified / UNKNOWN

- Official GrapheneOS, or any unofficial build, actually booting on the **REDMAGIC 11S Pro**
- Whether GrimoireOS boots reliably on the 11 Pro+, and whether it includes Hexagon / QNN libraries that work
- Whether `EXECUTE_APP_FUNCTIONS` and AppFunctions survive in GrapheneOS and LineageOS 23 trees
- LiteRT / GenieX behaviour under GrapheneOS SELinux on Snapdragon
- MTE quality on SM8850 / 11S Pro
- An official LineageOS build for the 11S Pro
- Current Google GMS licensing for custom ROMs (not re-opened)
