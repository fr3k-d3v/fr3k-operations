---
id: EXP-2026-012
title: "IBM ContextForge v1.1.2 as an MCP gateway, isolated evaluation"
related_entry: FBR-2026-001
status: queued
priority: "P3 (61–90 days)"
created_date: 2026-11-28
acceptance_criteria_defined: true
run_started: ""
run_completed: ""
environment: isolated / non-production (required)
---

# Experiment: IBM ContextForge v1.1.2 as an MCP gateway, isolated evaluation

**Acceptance criteria are defined below, before any run.** Never execute untrusted source code on production infrastructure, data, credentials or networks. Use an isolated test handset or container with no personal accounts.

Source finding: [radar 2026-11-27](../radar/2026-11-27.md), find 3. All upstream performance figures are CLAIM until reproduced here.

## Hypothesis

Label: HYPOTHESIS. IBM ContextForge v1.1.2 ([release](https://github.com/IBM/mcp-context-forge/releases/tag/v1.1.2), Apache-2.0 per the project) can front a small set of MCP servers with authentication, per-scope access checks and live list-changed events, with acceptable overhead. None of the release's features have been tested by us.

## Environment

- An isolated container or virtual machine with no production data, credentials or network access to production systems
- ContextForge pinned to v1.1.2 by tag and image digest, with two dummy MCP servers
- Source and dependencies reviewed before the first run (supply-chain review recorded)

## Acceptance criteria

1. [ ] Supply-chain review recorded: licence files, dependency list, container image provenance.
2. [ ] Two dummy MCP servers registered. A client lists and calls tools through the gateway.
3. [ ] Per-scope authorisation blocks a call that the token scope does not allow.
4. [ ] A list-changed event (`subscriptions/listen`) reaches a subscribed client when a tool is added, and per-principal stream limits are enforced.
5. [ ] Added latency per call, measured over 100 calls against a direct call, with the method recorded.
6. [ ] No real credentials, hostnames or tokens are used or committed.

## Method

Run entirely in the isolated environment. Record negative findings (setup failures, missing features, documentation gaps).

## Dependencies

None.

## Results

Not run.

## Outcome

- Pass / fail against acceptance criteria: not run
