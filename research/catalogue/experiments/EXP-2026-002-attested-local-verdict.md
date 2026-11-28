---
id: EXP-2026-002
title: "AI trust layer: attested local APK verdict (no root)"
related_entry: FBR-2026-001
status: queued
priority: "P1 (0–30 days)"
created_date: 2026-11-22
acceptance_criteria_defined: true
run_started: ""
run_completed: ""
environment: isolated / non-production (required)
---

# Experiment: AI trust layer: attested local APK verdict (no root)

**Acceptance criteria are defined below, before any run.** Never execute untrusted source code on production infrastructure, data, credentials or networks. Use an isolated test handset with no personal accounts.

## Hypothesis

Label: HYPOTHESIS. A Keystore-attested key can provide device and key provenance and tamper-evidence for a locally produced APK verdict, verifiable off-device to Google hardware roots without Play Integrity. It does NOT prove which model produced the verdict.

## Environment

- Devices: REDMAGIC 11S Pro and one Pixel (baseline), both stock and locked
- Verifier app V (FR3K-built): Keystore EC P-256 key with attestation challenge; StrongBox if available, else TEE; small local model plus deterministic rules
- Off-device checker S: JVM service on a laptop using android/keyattestation (Apache-2.0); never on production infrastructure
- Gate app G: requests a fresh challenge and grants a dummy feature only if S passes, the rules pass and the model says allow
- Test APKs: FR3K-built benign and synthetic risky APKs only; no live malware in this experiment

## Acceptance criteria

1. [ ] S validates V's chain to a Google hardware root (both current roots trusted) with the revocation list checked, and attestationSecurityLevel is TrustedEnvironment or StrongBox (record which; record StrongBox availability per device).
2. [ ] A stale-challenge replay is rejected 10/10.
3. [ ] A verdict modified by one byte is rejected 10/10.
4. [ ] A verdict signed by a non-attested software key is rejected 10/10.
5. [ ] The same APK scanned 20 times gives an identical model verdict 20/20 (greedy decoding, pinned model hash).
6. [ ] 10 APKs with injected benign cover-story strings and a risky permission set: G denies at least 9/10 because deterministic rules veto regardless of the model.
7. [ ] Scan, sign and verify round trip under 30 s for an APK under 50 MB on the 11S Pro (measure).
8. [ ] Packet capture shows no network traffic from V except the verdict to S.

## Method

V computes the APK SHA-256, the signing certificate digest, the permission list and selected strings. It runs the rules and the model, builds JSON {apk_hash, cert_digest, rule_hits, model_id, model_hash, decoding, verdict, challenge, timestamp} and signs it. S verifies the chain, the challenge, verifiedBootState, attestationApplicationId and the signature. Do not commit raw attestation chains (they contain device-unique data).

## Results

Not run.

## Outcome

- Pass / fail against acceptance criteria: not run
