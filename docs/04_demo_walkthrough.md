# Demo walkthrough

Run:

```bash
tof-workbench run
```

You will get JSON artifacts in:
- `01_intake/`
- `02_evidence/`
- `03_hypotheses/`
- `04_extracts/`
- `05_mapping/`
- `06_review/`
- `07_reports/`

Then inspect `07_reports/run_summary.json` and `07_reports/acceptance.json`.

The demo is intentionally small, but it shows the core pattern:
legacy input -> evidence -> hypotheses -> split extracts -> mapping -> review/report.
