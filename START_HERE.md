# Start here

`tof-legacy-recovery-workbench` is a **recovery and separation tool** for older mixed material.

> German version: [START_HERE_DE.md](START_HERE_DE.md)

Its job is to preserve provenance and uncertainty before anything moves into planning or implementation.

## Pipeline

```text
00_input_alt/
  → 01_intake/
  → 02_evidence/
  → 03_hypotheses/
  → 04_extracts/
  → 05_mapping/
  → 06_review/
  → 07_reports/
```

The stages deliberately separate observations from interpretation.

## Requirements

- Python 3.11+
- optionally Docker with Docker Compose

## First local run

Clone once:

```bash
git clone https://github.com/IMaugrenI/tof-legacy-recovery-workbench.git
cd tof-legacy-recovery-workbench
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
tof-workbench run
```

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
tof-workbench run
```

## Docker alternative

```bash
docker compose up --build werkbench
```

## What belongs in `00_input_alt/`

Only put material there that you intentionally want the recovery process to inspect.

For a public clone or public issue, use synthetic/public-safe material. Do not commit private runtime exports, secrets, customer data, or personal case material.

## What success looks like

A good run should make it easier to distinguish:

- neutral evidence
- hypotheses
- extracted candidate material
- stable target classifications
- items that still require review

The default recovery path must not silently generate or release target runtime code.

## What comes next

If recovered material is sufficiently prepared, it can move into [tof-bridge-planning-method](https://github.com/IMaugrenI/tof-bridge-planning-method).

Recovery itself is not planning approval and not runtime truth.

## Security / privacy

Read [SECURITY.md](SECURITY.md) before using non-public material.
