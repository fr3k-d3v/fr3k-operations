---
id: EXP-2026-005
title: "AppFunctions provider and caller interop"
related_entry: FBR-2026-001
status: queued
priority: "P2 (31–60 days)"
created_date: 2026-11-22
acceptance_criteria_defined: true
run_started: ""
run_completed: ""
environment: isolated / non-production (required)
---

# Experiment: AppFunctions provider and caller interop

**Acceptance criteria are defined below, before any run.** Never execute untrusted source code on production infrastructure, data, credentials or networks. Use an isolated test handset with no personal accounts.

## Hypothesis

Label: HYPOTHESIS. FR3K tools can be exposed as AppFunctions; caller access for a sideloaded agent may be restricted.

## Environment

- Android 16+ device (Pixel baseline, then the REDMAGIC)

## Acceptance criteria

1. [ ] FR3K provider functions are discoverable and executable through adb and Google's test agent.
2. [ ] Whether EXECUTE_APP_FUNCTIONS is grantable to a sideloaded app is determined and recorded (pass means a definitive answer).
3. [ ] One tool schema is generated to both MCP and AppFunctions from a single definition.

## Method

Use the Jetpack AppFunctions library (alpha); record API surface changes.

## Results

Not run.

## Outcome

- Pass / fail against acceptance criteria: not run
