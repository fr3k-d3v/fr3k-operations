---
id: EXP-2026-003
title: "Tier C no-root agent MVP"
related_entry: FBR-2026-001
status: queued
priority: "P1 (0–30 days)"
created_date: 2026-11-22
acceptance_criteria_defined: true
run_started: ""
run_completed: ""
environment: isolated / non-production (required)
---

# Experiment: Tier C no-root agent MVP

**Acceptance criteria are defined below, before any run.** Never execute untrusted source code on production infrastructure, data, credentials or networks. Use an isolated test handset with no personal accounts.

## Hypothesis

Label: HYPOTHESIS. A launcher plus AccessibilityService plus local model can complete common phone tasks with no cloud calls, at an acceptable success rate.

## Environment

- REDMAGIC 11S Pro, test account only
- Local model through the best runtime from EXP-001; MCP endpoint on localhost

## Acceptance criteria

1. [ ] At least 14/20 scripted tasks (alarms, notes, settings toggles, messaging to a test contact) complete.
2. [ ] Zero cloud calls (packet capture).
3. [ ] Every write action requires on-device confirmation, and the audit log records each tool call.
4. [ ] The agent auto-pauses in a designated sensitive-app list.
5. [ ] Play Integrity appAccessRiskVerdict effect recorded using an FR3K test app (or UNKNOWN if a Play-distributed test app is not available).

## Method

Scripted tasks run 3 times each. Record failures by cause (perception, planning, action).

## Results

Not run.

## Outcome

- Pass / fail against acceptance criteria: not run
