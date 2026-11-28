# FR3K BLACKSITE RESEARCH catalogue

Versioned research catalogue for FR3K BLACKSITE RESEARCH: frontier technology discovery, scientific research, competitive intelligence and experimental engineering for FR3KD3V.

The purpose is not collecting links. Every useful discovery must produce an engineering hypothesis, test plan or concrete recommendation, and must be recorded here.

**This repository is public.** Do not record secrets, credentials, tokens, private hostnames, unreleased product internals, or other material that should remain private. Follow [SECURITY.md](../../SECURITY.md) and the public/private separation in the [root README](../../README.md).

The catalogue began as templates and an empty index and now holds its first entry, reports, experiments and radar digests. Do not invent entries, citations or performance claims.

## Layout

- [INDEX.md](INDEX.md) — register of catalogue entries
- [templates/](templates/) — entry, experiment and report templates
- [entries/](entries/) — one markdown file per discovery
- [experiments/](experiments/) — experiment queue and completed test records
- [reports/](reports/) — deep dives, comparisons and licence reports; weekly deep dive, competitor watch and FR3K advantage reports
- [radar/](radar/README.md) — dated radar digests and standing watch logs

Existing operations open-source inventory remains at the [research folder root](../README.md) and in [docs/research](../../docs/research/repositories.md). Do not overwrite those files.

## Validation pipeline

DISCOVER → SOURCE → REPRODUCE → BENCHMARK → COMPARE → EXPERIMENT → RECOMMEND → RECORD

1. **DISCOVER** — find a candidate from any source, including low-star and recently created work. Do not dismiss early-stage work because it is unpopular; do not recommend it merely because it is obscure.
2. **SOURCE** — record original source, author, date, licence, maintenance activity and authenticity.
3. **REPRODUCE** — attempt reproduction in isolation. Flag any result that has not been reproduced.
4. **BENCHMARK** — measure performance, quality, resource use and failure rates against published claims, using a recorded methodology.
5. **COMPARE** — compare with current FR3K methods and realistic alternative approaches.
6. **EXPERIMENT** — run controlled tests only after acceptance criteria are written. Prefer low-cost, open-source, locally runnable approaches.
7. **RECOMMEND** — state a concrete integration recommendation, estimated cost and commercial relevance, or an explicit reject/defer decision.
8. **RECORD** — add or update the catalogue entry, index row and any linked experiment or report. Avoid duplicates and stale records.

## Evidence labels

Label every material statement. Do not blur these categories.

| Label | Meaning |
|---|---|
| CLAIM | Asserted by a source; not independently established here |
| OBSERVATION | Directly observed by the researcher |
| EVIDENCE | Material that supports or contradicts a claim or observation |
| VERIFIED FACT | Corroborated by evidence and independently established |
| HYPOTHESIS | A testable proposition; not yet established |
| SIMULATION | Result of a model, estimate or simulated workload, not a live measurement |
| UNKNOWN | Not checked |

A commit is not a deployment. A published benchmark is not a reproduced benchmark. Flag unreproduced results clearly in the entry front matter (`reproduced: false`) and in the body.

## Confidence levels

| Level | Meaning |
|---|---|
| unverified | Claims or first-pass discovery only; not reproduced |
| low | Source reviewed; limited corroboration; not independently reproduced |
| medium | Sourced and partially corroborated; reproduction incomplete or narrow |
| high | Independently reproduced and benchmarked under a recorded method |
| confirmed | Reproduced, benchmarked and compared under controlled conditions that meet pre-written acceptance criteria |

Confidence must not exceed the evidence. Unreproduced work cannot be rated above `low`.

## Recording rules

- **No fabrications.** Do not invent citations, dates, licences, authors, benchmarks or performance figures.
- **No unverified performance claims.** Report published numbers as CLAIM until measured. Record claimed versus measured performance separately.
- **Flag unreproduced results.** If reproduction has not been completed, say so. Do not imply verification.
- **Deduplicate.** Before adding an entry, search [INDEX.md](INDEX.md) and `entries/` for the same source, artefact or substantially identical approach. Update the existing record instead of creating a parallel one. Note forks and renames in the original entry.
- **Prevent staleness.** Review entries when sources change, when a reproduction or benchmark is completed, and during routine catalogue maintenance. Mark abandoned, superseded or time-expired records `status: stale` and record the reason and the review date. Do not leave outdated performance claims unmarked.
- **Separate implementation from recommendation.** A recommendation is not an integration.
- **Licence and supply-chain diligence.** Record licence, authenticity and security, privacy and supply-chain risk. API licence metadata is insufficient for adoption.

## Experimental safety

Never execute untrusted source code directly on production infrastructure. Use isolation and appropriate review. Do not run untrusted code against production data, credentials or networks.

Define acceptance criteria before running tests. Compare realistic workloads and hardware configurations. Record performance, thermal behaviour, memory use, cost, quality, failure rates, negative findings and reproducibility details.

## Entry identifiers

Use `FBR-YYYY-NNN` (FR3K BLACKSITE RESEARCH, year, zero-padded sequence). Assign the next unused number for that year from [INDEX.md](INDEX.md). Filenames: `FBR-YYYY-NNN-short-slug.md` in `entries/`.

Dates are ISO 8601 (`YYYY-MM-DD`) in Australia/Brisbane time (UTC+10).

## Status and routing

Status: `draft` | `discovered` | `sourced` | `reproduction-pending` | `reproduced` | `benchmarked` | `compared` | `recommended` | `deferred` | `rejected` | `stale`

Routing:

- **KINGPIN DEV** — implementation-ready findings
- **MONEY MACHINE** — revenue-relevant opportunities

An entry may be routed to one, both, or neither. Routing does not replace the written recommendation.

## How to add a record

1. Copy [templates/entry.md](templates/entry.md) to `entries/`.
2. Fill front matter and body. Leave unknowns as `UNKNOWN` rather than guessing.
3. Add a row to [INDEX.md](INDEX.md).
4. If an experiment is required, add it to [experiments/QUEUE.md](experiments/QUEUE.md) from [templates/experiment.md](templates/experiment.md), with acceptance criteria written first.
5. File reports under `reports/` using the report templates.
