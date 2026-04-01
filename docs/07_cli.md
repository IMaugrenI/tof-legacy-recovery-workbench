# CLI

## Commands

### Run the full pipeline

```bash
tof-workbench run
```

### Run acceptance only

```bash
tof-workbench acceptance
```

### Remove generated stage directories

```bash
tof-workbench clean
```

## Expected output

The default run writes append-only JSON artifacts into:
- `01_intake/`
- `02_evidence/`
- `03_hypotheses/`
- `04_extracts/`
- `05_mapping/`
- `06_review/`
- `07_reports/`
