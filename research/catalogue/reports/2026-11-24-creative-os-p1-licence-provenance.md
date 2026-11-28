---
type: licence-provenance
report_date: 2026-11-24
author: FR3K BLACKSITE RESEARCH
topic: Licence and provenance deep dive for the Creative OS P1 character vertical slice
reproduced: false
checked_at: "24 November 2026, afternoon AEST (Australia/Brisbane)"
scope: research-only; no clone-and-run, no builds, no code import
not_legal_advice: true
---

# Creative OS P1: licence and provenance of character-pipeline candidates

Prepared 24 November 2026, afternoon AEST (Australia/Brisbane). Research only. Sources were read through the GitHub API, `raw.githubusercontent.com`, project websites, and a local inventory of FR3K project trees. No candidate was cloned for execution, built, or imported.

This is **not legal advice**. Dispositions are engineering recommendations. A qualified solicitor should review any product that will be distributed.

Label key: **VERIFIED** = read from a primary file or official API this turn. **EVIDENCE** = a cited primary source. **OBSERVATION** = what was or was not present in the trees examined. **CLAIM** = a project's own marketing or README statement, not independently reproduced.

Priority path in scope: owned asset → sprite atlas / GLB → rig → voice / viseme lip-sync → real Android overlay.

## Findings in one page

| Candidate | Source | Licence (code) | Disposition | One-line reason |
|---|---|---|---|---|
| FR3K Waifu Studio + Android overlay | Local trees only; not in public `fr3k-d3v` | No `LICENSE` file; `package.json` is `"private": true` (treat as all rights reserved) | **ADOPT** the code path; **BLOCKED** current catalogue assets | Already the Filament GLB overlay; Waifu3D-sourced parts are marked `local-personal` |
| SENTIENCE | — | — | **NOT FOUND** | Not in public `fr3k-d3v` repos, and no matching tree on this box |
| OpenBone (UXCentury) | [UXCentury/open-bone](https://github.com/UXCentury/open-bone) | MIT | **ADAPT** (2D path) | Permissive editor plus an `openbone-android` module; not a drop-in for the existing 3D GLB overlay |
| OpenBone (Samlinb) | [Samlinb/openbone](https://github.com/Samlinb/openbone) | No `LICENSE` file | **REFERENCE_ONLY** | Unlicensed Spine-format editor; hero demo assets may not be redistributed |
| Rigby2D | [jaisurya-dev-art/rigby2d](https://github.com/jaisurya-dev-art/rigby2d) | MIT OR Apache-2.0 | **ADAPT** (2D rig + lip-sync tool) | Permissive, active, audio lip-sync; no first-party Android runtime |
| Stickman-Studio (saiedpod-bot) | [saiedpod-bot/Stickman-Studio](https://github.com/saiedpod-bot/Stickman-Studio) | No `LICENSE` file | **REFERENCE_ONLY** | Unlicensed YouTube/slideshow pipeline, not an overlay runtime |
| Stickman-Studio (atharv01h) | [atharv01h/Stickman-Studio](https://github.com/atharv01h/Stickman-Studio) | MIT | **REDUNDANT** | Offline shorts generator; Kokoro / model-weight terms are separate |
| OpenMimicry | [Gabriel382/openmimicry](https://github.com/Gabriel382/openmimicry) | MIT (code only) | **REFERENCE_ONLY** | Useful contracts; Android is roadmap-only; Piper extra is GPL-3.0; fan packs are non-commercial |
| desktop-buddy (camzymb) | [camzymb/desktop-buddy](https://github.com/camzymb/desktop-buddy) | No `LICENSE` file | **REFERENCE_ONLY** | Unlicensed desktop Python companion; not Android |
| claude-desktop-buddy | [anthropics/claude-desktop-buddy](https://github.com/anthropics/claude-desktop-buddy) | GitHub SPDX `NOASSERTION` | **REDUNDANT** | BLE hardware reference, not a character pipeline |
| Sprixy | [PetitOursManu/Sprixy](https://github.com/PetitOursManu/Sprixy) | MIT | **REFERENCE_ONLY** | New MIT asset studio; not AGPL; generated-art terms follow the chosen API |
| SpriteKiln (LucasJRamos) | [LucasJRamos/spritekiln](https://github.com/LucasJRamos/spritekiln) | MIT (code); CC0 examples; ARR showcase | **ADAPT** (atlas tool) | Permissive sprite-atlas generator; do not reuse showcase art |
| SpriteKiln (brunocpf) | [brunocpf/spritekiln](https://github.com/brunocpf/spritekiln) | GPL-3.0 | **BLOCKED** (import) | Same name, different project; copyleft; not AGPL |
| 3DGenStudio | [visualbruno/3DGenStudio](https://github.com/visualbruno/3DGenStudio) | Custom Community Licence (source-available) | **ISOLATE** as an internal tool; **BLOCKED** from product bundles | No resale, no paid hosting, no paid bundle of the software itself |

**AGPL signal (task note):** no AGPL licence text was found in Sprixy or in LucasJRamos/spritekiln. The nearby copyleft facts are brunocpf/spritekiln at **GPL-3.0**, OpenMimicry's optional Piper extra at **GPL-3.0**, and [3DGenStudio issue #5](https://github.com/visualbruno/3DGenStudio/issues/5), where AGPL was proposed and **rejected** by the author.

## Method and limits

- `fr3k-d3v` is a GitHub **User** account, not an organisation. A `user:fr3k-d3v` search on 24 November 2026 returned **9 public repositories**. None are named or described as SENTIENCE, waifu, overlay, or viseme. **UNKNOWN:** whether private repositories exist; this search did not list any.
- The Creative OS opportunity plan document was **not found** in the local project trees or readable agent stores.
- No matching originals for the named candidates were found on Codeberg in a web search this turn.
- Times below are converted to AEST (Australia/Brisbane, UTC+10).

---

## 1. Existing FR3K SENTIENCE / Waifu / voice / overlay work

### 1.1 What was found

**OBSERVATION:** two local projects implement the current character path. Neither has a public GitHub remote in the trees examined.

**FR3K Waifu Studio** (local project tree, private npm package).

- **EVIDENCE:** `package.json` sets `"private": true` and has no `license` field. There is no `LICENSE` file in the project root.
- **VERIFIED:** the local git history has a baseline commit dated 22 November 2026 and **no remotes**.
- Stack: React 19, Three.js 0.181, React Three Fiber / Drei, Vite, TypeScript. A `voice.ts` module uses the browser `speechSynthesis` and `SpeechRecognition` APIs, with recognition language `en-AU`.
- Private assets are gated by `privateCharacter.ts`. A manifest must declare `rights: 'local-personal' | 'redistributable'`, a SHA-256, a local path under `/private-assets/`, and a provenance `source` string. VRM and GLB are allowed in that studio manifest.

**FR3K Android overlay** (local Android project tree).

- **OBSERVATION:** no `LICENSE` file and no `.git` directory in this checkout.
- **VERIFIED:** Gradle depends on Filament 1.68.2 (`filament-android`, `gltfio-android`, `filament-utils-android`) and AndroidX Media3 ExoPlayer 1.5.1, pulled as Maven artefacts rather than vendored source.
- **VERIFIED:** [Filament v1.68.2 `LICENSE`](https://raw.githubusercontent.com/google/filament/v1.68.2/LICENSE) is Apache Licence 2.0.
- **VERIFIED:** `CharacterModelLibrary.kt` refuses `.vrm` imports and requires a standard glTF 2.0 `.glb`. Metadata records `tts_locale=en-AU`.
- **VERIFIED:** `FilamentCharacterView.setVoicePhase` selects a **named animation clip** via `CharacterAnimationSelector.forPhase`. That is phase-to-clip mapping (idle / listen / speak), not phoneme viseme or morph-target lip-sync.
- **OBSERVATION:** `OverlayService.kt` references `AndroidCreatureSpeech`, `CreatureVoiceSession`, `CreatureBackgroundAudioGate`, `VoicePhase`, `OverlayMediaSurface` and `Track`, but those source files are **not present** in the local checkouts examined. This checkout looks incomplete for the voice layer.
- Direct Studio npm dependencies are ordinary permissive libraries (React, Three, Vite, Zustand, `ws`). **EVIDENCE:** `jszip` is [dual-licensed MIT or GPLv3](https://github.com/Stuk/jszip/blob/main/LICENSE.markdown); the tree may use the MIT choice. No Live2D Cubism SDK, no VRM runtime, and no vendored TTS weight files were found in the source trees (private asset binaries were not inventoried beyond licence/rights fields).

**Waifu3D catalogue (assets, not FR3K code).**

- **VERIFIED:** the Studio's private-asset source catalogue and its evidence copy both declare a user-local Waifu3D application installation as the source and `rights=local-personal`.
- **EVIDENCE:** the Studio's own verification note (21 November 2026) states that the installed Waifu3D application's assets and APK stay on the owner's local machine and are **not redistributable** through the repository.
- **CLAIM (third party):** [Waifu 3D Engine](https://thejoigame.itch.io/waifu3dengine) by TheJOIGame is a closed, offline Android character creator distributed from itch.io / Patreon. No OSI licence text was found for that application or its bundled parts.
- **Disposition of those assets: BLOCKED** for shipping, publication, or commercial use until the rights holder grants a redistribution licence. The Studio manifest already has a `redistributable` flag for a replacement owned GLB.

### 1.2 SENTIENCE

**NOT FOUND.** Searches of public `fr3k-d3v` repositories, the local project trees and readable stores for `sentience` returned no project tree. If it lives in a private repository or another account, that location was not visible this turn.

### 1.3 Recommended disposition

- **ADOPT** the existing Studio + Filament overlay as the P1 runtime (Kotlin/Android, `SYSTEM_ALERT_WINDOW`, arm64-v8a-capable via Filament AAR).
- **BLOCKED:** Waifu3D-sourced meshes, textures, and parts.
- **REIMPLEMENT:** viseme / lip-sync and the missing Android speech types; do not import a Live2D proprietary SDK.
- Add a `LICENSE` before any public repository. Keep `private-assets` out of git (already the local design).

---

## 2. Named external candidates

### 2.1 OpenBone — two different projects

**A. UXCentury/open-bone** (recommended if "OpenBone" means a 2D skeletal tool).

- Author: UXCentury. Created 9 November 2026, 12:38am AEST. Last push 24 November 2026, 7:06am AEST. **16** stars, **0** open issues, TypeScript / Tauri / SolidJS. Site: [openbone.io](https://openbone.io).
- **VERIFIED:** [`LICENSE`](https://raw.githubusercontent.com/UXCentury/open-bone/main/LICENSE) is MIT, "Copyright (c) 2026 UX Century and OpenBone contributors". GitHub SPDX: MIT. README states the project is MIT end-to-end and forbids GPL/AGPL/non-commercial dependencies in contributions.
- **VERIFIED:** `runtimes/java/openbone-android/` exists. Other runtimes include C++, C#, Flutter, Haxe, Swift, and libGDX.
- Compatibility: 2D skeletal (Spine-style rigging, Rive-style state machines, MCP). Complements, rather than replaces, the 3D GLB Filament overlay.
- **ADAPT** for a 2D atlas/rig overlay path. **CLAIM** (README, not reproduced here): example art/sound used ElevenLabs and Canva and is credited separately from the MIT code.
- Risks: young project; example asset licences must be checked path-by-path; FFmpeg is documented as an unsbundled LGPL/GPL external binary.

**B. Samlinb/openbone**

- Author: Samlinb. Created 25 October 2026, 2:48pm AEST. Last commit 14 November 2026, 3:28pm AEST (`c7e9a080`). **2** stars, Java 17 / Swing / libGDX, Spine 4.2-subset JSON workflow.
- **VERIFIED:** the default-branch root listing has **no** `LICENSE` or `COPYING` file. GitHub licence field is empty. Treat as all rights reserved.
- README says the project includes no official Spine Runtime source, uses a supported subset of the Spine JSON format, and that hero demonstration assets "stay local because their demonstration license prohibits redistribution." Native `.spine` conversion "requires a separately configured licensed CLI."
- **REFERENCE_ONLY.** Do not import. Format-compatibility work is not a licence to use Spine.

### 2.2 Rigby2D

- Author: jaisurya-dev-art. [jaisurya-dev-art/rigby2d](https://github.com/jaisurya-dev-art/rigby2d). Created 13 October 2026, 5:54pm AEST. Last commit on `develop` 23 November 2026, 11:41pm AEST (`f538339`, "Runtimes: SDL3 and community runtimes"). **346** stars, **41** forks, **2** open issues. JavaScript / Tauri / Rust. Docs: [rigby2d.com/docs](https://rigby2d.com/docs).
- **VERIFIED:** dual [`LICENSE-MIT`](https://raw.githubusercontent.com/jaisurya-dev-art/rigby2d/develop/LICENSE-MIT) ("Copyright (c) 2026 jaisurya-dev-art") and `LICENSE-APACHE`. GitHub's licence field shows only Apache-2.0, which is a **licence-metadata mismatch** (the files are a standard dual grant).
- Runtimes present: Godot, Unity, Cocos, Defold, Phaser, Pixi, Ren'Py, Rust, SDL3. **OBSERVATION:** no first-party `android` or `kotlin` runtime directory. Android would be via Unity/Godot/Cocos export, or a new runtime.
- **CLAIM** (repo description, not reproduced): AutoRig from layered PSDs, IK, physics, **lip-sync from audio**, MCP server, JSON/`.skel` export.
- **ADAPT** as the 2D rig / lip-sync authoring tool. Do not replace the Filament GLB overlay with it unless P1 explicitly switches to 2D.

### 2.3 stickman-studio — two later projects, same name

**A. saiedpod-bot/Stickman-Studio** (older, more stars). Created 23 June 2026, 9:51pm AEST. Last push 27 June 2026, 9:57am AEST. **55** stars, **18** forks, Python / Streamlit, Gemini / Imagen / edge-tts / ffmpeg / YouTube pipeline.

- **VERIFIED:** root listing has **no** `LICENSE` file. GitHub `license` is `null`. **REFERENCE_ONLY.** Wrong problem for P1 (video production, not a live overlay). Stale after June 2026.

**B. atharv01h/Stickman-Studio**. Created 11 November 2026, 11:31pm AEST. Last push 21 November 2026, 1:27am AEST. **13** stars. Offline "faceless" shorts studio.

- **VERIFIED:** [`LICENSE`](https://raw.githubusercontent.com/atharv01h/Stickman-Studio/main/LICENSE) is MIT, "Copyright (c) 2026 Atharv Hatwar".
- **REDUNDANT** for the Android overlay path. If any TTS weights (the topic list names Kokoro) were bundled, those licences are separate and were not audited this turn.

### 2.4 OpenMimicry

- Author: Gabriel Henrique Alencar Medeiros ([Gabriel382](https://github.com/Gabriel382)). Created 16 March 2026, 4:52am AEST. Last commit 23 July 2026, 12:55am AEST (`825aa745`). **3** stars, **3** open issues. Python FastAPI + React + Tauri. Validated on Windows 11; Linux/macOS pending. **CLAIM:** Android is on the public roadmap, not in the validated release (v0.5.1 beta).
- **VERIFIED:** [`LICENSE`](https://raw.githubusercontent.com/Gabriel382/openmimicry/main/LICENSE) is MIT, "Copyright (c) 2026 OpenMimicry contributors".
- **VERIFIED:** [`docs/licensing.md`](https://raw.githubusercontent.com/Gabriel382/openmimicry/main/docs/licensing.md) says MIT does **not** relicense dependencies, model weights, voice files, or character art. The "commercial profile" uses Faster-Whisper, **host OS TTS**, and OpenRouter/Ollama, and excludes Piper, Chatterbox, Hindsight, and ElevenLabs. It states the current Piper application code is **GPL-3.0**, and that voice-model cards can impose different terms. Character packs need a `license` field; commercial mode rejects GPL/AGPL, non-commercial, and CC-BY-NC labels by default.
- **CLAIM** (author, LinkedIn / README): experimental GLaDOS, JARVIS, and Paimon packs are unofficial, personal, non-commercial fan work.
- **REFERENCE_ONLY** for architecture (replaceable TTS/LLM/avatar contracts, commercial vs community profiles). Do not import community extras, fan packs, or Piper into a proprietary Android app. The project has not moved in about four months.

### 2.5 desktop-buddy — name collision

The string matches many unrelated repositories. Two were assessed for this brief.

**A. camzymb/desktop-buddy** (closest character companion). Created 28 May 2026, 1:26am AEST. Last push 10 June 2026, 9:01pm AEST. **2** stars. Python desktop companion with a custom-illustrated character, voice clips, Calendar/Gmail.

- **VERIFIED:** root listing has no `LICENSE` / `COPYING` / `NOTICE`. GitHub `license` is `null`. Sprites and assets are in-tree without a visible asset licence.
- **REFERENCE_ONLY** (all rights reserved; art provenance unclear; not Android).

**B. anthropics/claude-desktop-buddy**. **2721** stars. C++ BLE / hardware "desk pet" reference for Claude Desktop. GitHub SPDX `NOASSERTION`. Last push 17 April 2026, 9:25am AEST.

- **REDUNDANT** for atlas/GLB/viseme/Android overlay.

### 2.6 Sprixy

- Author: PetitOursManu. Created 23 November 2026, 8:56am AEST. Last commit 24 November 2026, 7:23am AEST (`b4801191`). **0** stars, **0** issues. TypeScript monorepo, self-hosted 2D asset studio, BYOK to fal.ai / OpenRouter, REST + MCP.
- **VERIFIED:** [`LICENSE`](https://raw.githubusercontent.com/PetitOursManu/Sprixy/main/LICENSE) and `package.json` `"license": "MIT"` agree. Copyright "2026 Sprixy contributors". **Not AGPL.**
- **REFERENCE_ONLY** until it has a track record. Generated-image rights follow the upstream provider's terms, which were not audited per-provider this turn. No Android runtime.

### 2.7 SpriteKiln — two different projects, plus the AGPL note

**A. LucasJRamos/spritekiln** (original name-bearer, 177 stars). Created 22 October 2026, 5:25am AEST. Last commit 12 November 2026, 10:28pm AEST (`17ae0ea8`, docs for 0.4.0). Python, YAML procedural 3D → pixel-art sheets, MCP, Godot/Unity/MonoGame integrations. GitHub licence field: "Other" (mixed files, not a missing licence).

- **VERIFIED:** [`LICENSE`](https://raw.githubusercontent.com/LucasJRamos/spritekiln/main/LICENSE) and `REUSE.toml`:
  - code, docs, integrations: **MIT**, "Copyright (c) 2026 Lucas Ramos";
  - listed example assets: **CC0 1.0**;
  - showcase characters (Templar, Huntress / Hunt Tower, and other demonstration characters): **all rights reserved**, demonstration only (`LicenseRef-Showcase`).
- **ADAPT** as an atlas generator on a 2D path. Never vendor `showcase/` or Hunt Tower art. **Not AGPL.**

**B. brunocpf/spritekiln** (same name, not a GitHub fork). Created 22 October 2026, 11:05am AEST, one day after Lucas's repo. Last push the same day. **23** stars. ComfyUI nodes for local 2D game art.

- **VERIFIED:** [`LICENSE`](https://raw.githubusercontent.com/brunocpf/spritekiln/main/LICENSE) is the **GNU GPL v3** (29 June 2007 FSF text). GitHub SPDX: GPL-3.0. **Not AGPL**, but still copyleft: "The GNU General Public License does not permit incorporating your program into proprietary programs."
- **BLOCKED** for import or linking into a proprietary FR3K Android app. Using it only as a detached ComfyUI tool would still leave generated-asset and model-weight terms to audit; that path is **ISOLATE** at best.

### 2.8 3DGenStudio and similar unknown licences

- Author: visualbruno (Bruno Fargnoli). [visualbruno/3DGenStudio](https://github.com/visualbruno/3DGenStudio). Created 10 April 2026, 11:34pm AEST. Default-branch last commit 8 November 2026, 9:21pm AEST (`15ec59b4`, "version 4.1.0"). GitHub `pushed_at` is later (23 November 2026, 12:50am AEST) — **UNKNOWN** which ref that push moved. **817** stars, **113** forks, **6** open issues. JavaScript / Electron / ComfyUI. Site: [3dgenstudio.com](https://www.3dgenstudio.com). GitHub SPDX: `NOASSERTION`.

- **VERIFIED:** [`LICENSE`](https://raw.githubusercontent.com/visualbruno/3DGenStudio/main/LICENSE) is the "3D Gen Studio Community License". It grants use, copy, and modify for personal, educational, internal research, and commercial *use*, but **without prior written consent** you may not sell, rent, or lease the software or derivatives; host it as a paid public or private service or subscription; or resell it in a commercial package. It also says you own generated meshes, textures, and assets, and may sell those outputs. The same terms appear on [the website terms page](https://www.3dgenstudio.com/terms-and-conditions.html).
- **VERIFIED:** a separate `META-LLAMA-3-LICENSE` is in the repo. The README says optional Kimodo motion generation downloads Meta Llama 3-8B-Instruct under the Meta Llama 3 Community Licence (attribution, acceptable-use, and a 700-million-MAU clause). Kimodo itself is described as Apache-2.0; the SOMA checkpoint has NVIDIA model-card terms.
- **VERIFIED:** [issue #5](https://github.com/visualbruno/3DGenStudio/issues/5) (closed) proposed switching to AGPL-3.0. The author declined, because a no-resale rule is incompatible with OSI licences, and floated a standardised source-available alternative instead. The file in tree is still the custom Community Licence.
- **ISOLATE** as an optional internal workstation for generating meshes. **BLOCKED** from being shipped, hosted, or sold as part of a FR3K product. Output ownership still depends on the ToS of whatever ComfyUI models or APIs are used; those were not audited model-by-model this turn.

---

## 3. What this means for the P1 path

Keep the current **owned GLB → Filament Android overlay** as the vertical slice. The permissive 2D tools (UXCentury OpenBone, Rigby2D, Lucas SpriteKiln) are useful *beside* that path for atlas/rig work. They do not remove the need for a redistributable character, or for a viseme layer that this overlay does not yet have.

Avoid: unlicensed repos, Waifu3D-sourced parts, Live2D proprietary SDKs, Piper or other GPL TTS in the shipped APK, brunocpf SpriteKiln, 3DGenStudio as a product component, OpenMimicry fan packs, and SpriteKiln showcase art.

## 4. Owner decisions needed

1. Commission or export a character the owner actually has the right to redistribute, and mark the Studio manifest `rights=redistributable`. Keep the current Waifu3D catalogue off any public or commercial build.
2. Confirm whether a SENTIENCE repository exists (private GitHub or another machine). It was not found here.
3. Confirm which "OpenBone" and "desktop-buddy" were intended. This report treats UXCentury/open-bone and camzymb/desktop-buddy as the character-tool matches, and records the name collisions.
4. Decide whether P1 stays 3D GLB (Filament) or also stands up a 2D atlas runtime (`openbone-android` or a Rigby2D export).
5. Point KINGPIN at the missing Android speech sources, or accept a reimplementation of system TTS + visemes.
6. If 3DGenStudio will be used internally, record that it must not be bundled or hosted as a paid service, and have counsel review upstream model terms. This is not legal advice.

## 5. Not found or not fully verified

- SENTIENCE project; Creative OS opportunity plan document; any private `fr3k-d3v` repositories.
- Official redistribution terms for Waifu 3D Engine (none found; treated as proprietary).
- AndroidCreatureSpeech and related types (referenced, files absent from this checkout).
- AndroidX Media3 1.5.1 POM was not re-opened this turn (Filament 1.68.2 Apache-2.0 was).
- Per-model ToS for ComfyUI / fal.ai / OpenRouter / Kokoro / ElevenLabs outputs.
- Whether 3DGenStudio's later `pushed_at` refers to a non-default branch.
- anthropics/claude-desktop-buddy licence text (GitHub `NOASSERTION`; out of P1 scope).
- Codeberg/GitLab originals for these names (none located).
- Runtime quality, performance, or lip-sync accuracy of any candidate (not run).
