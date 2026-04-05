# tof-legacy-recovery-workbench

> English is the primary text in this repository. A German clone is available in `README_DE.md`.

Public_safe recovery workbench for older mixed material.

I use this repo to show how I separate evidence, preserve provenance, and avoid false certainty during recovery work.

## start_here

### local

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
tof-workbench run
```

### docker

```bash
docker compose up --build werkbench
```

## what_this_repo_does

1. reads legacy input from `00_input_alt/`
2. builds append_only JSON artifacts across fixed stages
3. detects Discord, bot, and repo_runtime signals
4. splits mixed findings instead of collapsing them into one truth
5. maps results into stable target classes
6. keeps review_required cases visible

## why_this_matters

1. old material is often mixed, partial, or misleading
2. provenance matters during recovery
3. uncertainty should stay visible
4. recovery is not the same thing as runtime truth
5. default runs should not silently generate target code

## pipeline

1. `00_input_alt/` = legacy input material
2. `01_intake/` = intake records per source
3. `02_evidence/` = neutral evidence layer
4. `03_hypotheses/` = open hypothesis bundles
5. `04_extracts/` = split extraction artifacts
6. `05_mapping/` = mapping into stable target classes
7. `06_review/` = review_required records
8. `07_reports/` = summaries and acceptance

## for_employers

This repo is useful if you want to see how I handle:

1. recovery of unclear legacy material
2. evidence_vs_interpretation separation
3. append_only thinking and provenance discipline
4. cautious workflows that do not overclaim certainty

## related_public_repos

- [`tof_bridge_planning_method`](https://github.com/IMaugrenI/tof-bridge-planning-method) — planning baseline after recovery
- [`tof_local_builder`](https://github.com/IMaugrenI/tof_local_builder) — local builder stack
- [`tof_local_knowledge`](https://github.com/IMaugrenI/tof_local_knowledge) — on_prem local knowledge system
