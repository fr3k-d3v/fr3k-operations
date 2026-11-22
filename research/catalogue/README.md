# FR3K BLACKSITE RESEARCH catalogue
The purpose is not collecting links. Every useful discovery must produce an engineering hypothesis, test plan or concrete recommendation, and must be recorded here.

This repository is public. Do not record secrets, credentials, tokens, private hostnames, unreleased product internals or other material that should remain private. See [Security and privacy](../../SECURITY.md).

The catalogue starts as templates and an empty index. Do not invent entries, citations or performance claims. The operations open-source inventory in the [parent folder](../README.md) is separate. Do not overwrite it.

## Layout

| Path | Role |
|---|---|
| [INDEX.md](INDEX.md) | Catalogue index. One row per entry. |
| [templates/](templates/entry.md) | Entry, experiment and report templates. Copy them; do not fill them with invented findings. |
| [entries/](entries/README.md) | One file per discovery. |
| [experiments/](experiments/README.md) | Experiment records and the [queue](experiments/QUEUE.md). |
| [reports/](reports/README.md) | Daily radar, weekly deep dive, competitor watch and FR3K advantage reports. |

Templates: [entry](templates/entry.md), [experiment](templates/experiment.md), [daily radar](templates/daily-radar.md), [weekly deep dive](templates/weekly-deep-dive.md), [competitor watch](templates/competitor-watch.md), [FR3K advantage](templates/fr3k-advantage.md).

## Validation pipeline
DISCOVER → SOURCE → REPRODUCE → BENCHMARK → COMPARE → EXPERIMENT → RECOMMEND → RECORD

| Step | Rule |
|---|---|
| DISCOVER | Record the candidate and its primary link. Do not dismiss early-stage work for being unpopular, and do not recommend it for being obscure. |
| SOURCE | Record author, licence, maintenance activity and authenticity from the primary source. |
| REPRODUCE | Repeat the stated method where it is safe to do so. Flag unreproduced results. Record the methodology. |
| BENCHMARK | Measure on a stated workload and hardware. Separate claimed numbers from measured numbers. |
| COMPARE | Compare with the current method on the same criteria. |
| EXPERIMENT | Run only against acceptance criteria written and committed before the run. |
| RECOMMEND | State practical advantage, integration cost and routing at the strength the evidence label supports. |
| RECORD | File the entry from the template, add a row to INDEX.md, and mark any superseded entry. |

## Evidence labels
Shared labels match the [repository evidence discipline](../../README.md): CLAIM = reported, OBSERVATION = directly observed, VERIFIED FACT = corroborated by evidence, HYPOTHESIS = to test, UNKNOWN = not checked. A citation is not verification.

Entry `confidence` applies to the recommendation. Each statement in the body keeps its own label. Unreproduced performance numbers stay CLAIM.

| Label | Meaning |
|---|---|
| CLAIM | Reported. Not independently checked. |
| OBSERVATION | Directly observed. |
| EVIDENCE | Corroborating artefact (log, measurement, commit, primary document). Citing it is not, by itself, a VERIFIED FACT. |
| VERIFIED FACT | Corroborated by evidence an independent reader can re-check. |
| HYPOTHESIS | To test. Not a result. |
| SIMULATION | Modelled or synthetic output. Not a measurement of the target system. |
| UNKNOWN | Not checked. |

## Confidence

| Level | Criteria |
|---|---|
| high | Primary source inspected, methodology recorded, and the result reproduced or independently corroborated. |
| medium | Primary source inspected. Reproduction is missing or partial. |
| low | Secondary report only, or the method is incomplete. |
| none | Not assessed. |

Do not raise confidence because a source is popular, or lower it because a source is obscure.

## Reproduction flag
Every entry carries `reproduced`: `yes`, `no` or `partial`. Unreproduced performance numbers stay CLAIM. Partial reproduction covers only the part repeated; the rest stays CLAIM.

## Deduplication and staleness
Search [INDEX.md](INDEX.md) before adding an entry. One entry per primary source. File it as `entries/YYYY-MM-DD-short-slug.md`.

Mark a replaced entry `superseded` and link the replacement in its change log. Do not delete the old file.

Review entries older than 90 days, and review again when the upstream source changes. Set `last_reviewed` when you do.

## Safety
Never execute untrusted source code on production infrastructure. Use an isolated virtual machine or container, and review the code before running it.

## Routing
Implementation-ready findings go to KINGPIN DEV. Revenue-relevant opportunities go to MONEY MACHINE. Set `routing` to `KINGPIN DEV`, `MONEY MACHINE`, `both` or `none`.

## Report cadence

| Report | Where | Purpose |
|---|---|---|
| Daily radar | `reports/YYYY-MM-DD-daily-radar.md` | Finds that day that warrant a next action. |
| Weekly deep dive | `reports/YYYY-MM-DD-weekly-deep-dive.md` | One focus, with acceptance criteria written before any test. |
| Experiment queue | [experiments/QUEUE.md](experiments/QUEUE.md) | Prioritised runs. Acceptance criteria defined before queueing. |
| Competitor watch | `reports/YYYY-MM-DD-competitor-watch.md` | What changed, and whether it is a genuine advancement or marketing. |
| FR3K advantage | `reports/YYYY-MM-DD-fr3k-advantage.md` | Capabilities to pursue, and items deferred or rejected. |

For a weekly deep dive, `YYYY-MM-DD` is the week starting date. Templates only; do not invent findings or citations.
