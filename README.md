# tof-legacy-recovery-workbench

> English is the primary text in this repository. A German clone is available in `README_DE.md`.

Public-safe recovery workbench baseline for reading older mixed material, separating useful substance, and mapping results into stable target classes.

## At a glance

- reads legacy input from `00_input_alt/`
- builds append-only JSON artifacts across fixed stages
- detects Discord, bot, and repo/runtime signals
- splits mixed findings instead of collapsing them into one truth
- maps results into stable target classes:
  - `discord`
  - `bot`
  - `repo`
  - `review_required`
- does **not** generate target code by default

## Why this repo exists

This repository is a public baseline for a recovery/workbench pattern:

- intake older or mixed sources
- preserve provenance
- separate evidence from interpretation
- keep uncertainty visible
- prepare reusable substance without pretending it is already active runtime truth

## What this repo is

- a reduced technical workbench baseline
- a runnable demo pipeline
- a public-safe example of legacy recovery and mapping discipline

## What this repo is not

- not the private working corpus
- not the full internal recovery space
- not runtime truth
- not automatic code generation
- not a blind migration tool

## Pipeline stages

1. `00_input_alt/` – legacy input material
2. `01_intake/` – intake records per source
3. `02_evidence/` – neutral evidence layer
4. `03_hypotheses/` – open-set hypothesis bundles
5. `04_extracts/` – split extraction artifacts
6. `05_mapping/` – mapping into stable target classes
7. `06_review/` – review-required records
8. `07_reports/` – summary, duplicates, acceptance

## Quick start

### Local

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
tof-workbench run
```

### Docker

```bash
docker compose up --build werkbench
```

## Demo input

The repository contains only public-safe fictional examples:

- a Discord channel note bundle
- a small bot module
- a compose-like runtime fragment
- an extensionless entrypoint file

## Key rules

- files without an extension are first-class input
- old hints are only hints, not truth
- open-set detection does not create new target classes
- target classes stay small and stable
- the default run does not materialize target code

## Related public repos

- [`tof_local_builder`](https://github.com/IMaugrenI/tof_local_builder) — local builder stack
- [`tof_local_knowledge`](https://github.com/IMaugrenI/tof_local_knowledge) — on-prem local knowledge system
- [`tof-bridge-planning-method`](https://github.com/IMaugrenI/tof-bridge-planning-method) — bridge-planning method layer
