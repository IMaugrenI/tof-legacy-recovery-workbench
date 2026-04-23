# tof-legacy-recovery-workbench

> English is the primary text in this repository. A German mirror is available in `README_DE.md`.

Public-safe recovery workbench for older mixed material.

I use this repo to show how I separate evidence, preserve provenance, and avoid false certainty during recovery work.

## What this repo is

This repository is a public method / transition repo for disciplined recovery of older mixed material.

## Who it is for

This repo is for technical readers who want to see how unclear or mixed legacy material can be separated carefully before planning or implementation.

## What it is not

This repo is not runtime truth, not implementation, and not a silent release path into target code.

## Where to go next

- `tof-showcase` — public architecture and product-line overview
- `tof-bridge-planning-method` — planning after recovery
- `tof-v7-public-frame` — tighter boundary reading for the later public frame

## Why this repo is public

I made this repo public because recovery work shows an important part of how I build.

I do not want to flatten or beautify older material. I want to read it carefully, separate it cleanly, preserve provenance, and keep uncertainty visible.

Recovery is not the same thing as runtime truth. This repo exists to show that I work methodically instead of mixing everything together.

## Start here

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

## What this repo does

1. reads legacy input from `00_input_alt/`
2. builds append-only JSON artifacts across fixed stages
3. detects Discord, bot, and repo-runtime signals
4. splits mixed findings instead of collapsing them into one truth
5. maps results into stable target classes
6. keeps review-required cases visible

## Why this matters

1. old material is often mixed, partial, or misleading
2. provenance matters during recovery
3. uncertainty should stay visible
4. recovery is not the same thing as runtime truth
5. default runs should not silently generate target code

## Pipeline

1. `00_input_alt/` = legacy input material
2. `01_intake/` = intake records per source
3. `02_evidence/` = neutral evidence layer
4. `03_hypotheses/` = open hypothesis bundles
5. `04_extracts/` = split extraction artifacts
6. `05_mapping/` = mapping into stable target classes
7. `06_review/` = review-required records
8. `07_reports/` = summaries and acceptance

## For employers

This repo is useful if you want to see how I handle:

1. recovery of unclear legacy material
2. evidence-vs-interpretation separation
3. append-only thinking and provenance discipline
4. cautious workflows that do not overclaim certainty

## Related public repos

- [`tof-bridge-planning-method`](https://github.com/IMaugrenI/tof-bridge-planning-method) — planning baseline after recovery
- [`tof_local_builder`](https://github.com/IMaugrenI/tof_local_builder) — local builder stack
- [`tof_local_knowledge`](https://github.com/IMaugrenI/tof_local_knowledge) — on-prem local knowledge system
