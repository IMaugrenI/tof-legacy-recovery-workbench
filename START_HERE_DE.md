# Hier starten

`tof-legacy-recovery-workbench` ist ein **Recovery- und Trennwerkzeug** für älteres gemischtes Material.

> English version: [START_HERE.md](START_HERE.md)

Seine Aufgabe ist, Herkunft und Unsicherheit zu erhalten, bevor etwas in Planung oder Implementierung weitergeht.

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

Die Stufen trennen Beobachtung bewusst von Interpretation.

## Voraussetzungen

- Python 3.11+
- optional Docker mit Docker Compose

## Erster lokaler Lauf

Einmal klonen:

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

## Docker-Alternative

```bash
docker compose up --build werkbench
```

## Was in `00_input_alt/` gehört

Lege dort nur Material ab, das du bewusst vom Recovery-Prozess untersuchen lassen willst.

Für öffentliche Klone oder Issues nur synthetisches bzw. public-safe Material verwenden. Keine privaten Runtime-Exporte, Geheimnisse, Kundendaten oder persönlichen Fallakten committen.

## Erfolgszustand

Ein guter Lauf soll klarer trennen:

- neutrale Evidenz
- Hypothesen
- extrahierte Kandidaten
- stabile Zielklassifikation
- weiterhin review-pflichtige Punkte

Der normale Recovery-Pfad darf nicht still Zielcode erzeugen oder veröffentlichen.

## Was danach kommt

Ausreichend vorbereitetes Material kann in [tof-bridge-planning-method](https://github.com/IMaugrenI/tof-bridge-planning-method) weitergehen.

Recovery ist selbst keine Planungsfreigabe und keine Runtime-Wahrheit.

## Sicherheit / Datenschutz

Vor nichtöffentlichem Material: [SECURITY.md](SECURITY.md).
