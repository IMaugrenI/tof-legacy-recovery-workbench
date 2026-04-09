# tof-legacy-recovery-workbench

> Die englische Hauptfassung liegt in `README.md`.

Public-safe Recovery-Workbench für älteres gemischtes Material.

Ich nutze dieses Repo, um zu zeigen, wie ich Evidenz trenne, Herkunft bewahre und falsche Sicherheit während Recovery-Arbeit vermeide.

## Warum dieses Repo öffentlich ist

Ich habe dieses Repo öffentlich gemacht, weil Recovery-Arbeit einen wichtigen Teil meiner Arbeitsweise zeigt.

Ich will altes Material nicht glätten oder schönreden. Ich will es sorgfältig lesen, sauber trennen, Herkunft bewahren und Unsicherheit sichtbar lassen.

Recovery ist nicht dasselbe wie Runtime-Wahrheit. Dieses Repo existiert, um zu zeigen, dass ich methodisch arbeite, statt alles einfach zu vermischen.

## Einstieg

### lokal

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

## Was dieses Repo macht

1. liest Legacy-Eingaben aus `00_input_alt/`
2. baut append-only JSON-Artefakte über feste Stufen hinweg
3. erkennt Discord-, Bot- und Repo-Runtime-Signale
4. trennt gemischte Funde statt sie in eine Wahrheit zusammenzufalten
5. mappt Ergebnisse in stabile Zielklassen
6. hält review_required-Fälle sichtbar

## Warum das wichtig ist

1. altes Material ist oft gemischt, unvollständig oder irreführend
2. Herkunft zählt bei Recovery-Arbeit
3. Unsicherheit muss sichtbar bleiben
4. Recovery ist nicht dasselbe wie Runtime-Wahrheit
5. Standardläufe dürfen nicht stillschweigend Zielcode erzeugen

## Pipeline

1. `00_input_alt/` = altes Eingabematerial
2. `01_intake/` = Intake-Datensätze pro Quelle
3. `02_evidence/` = neutrale Evidenzschicht
4. `03_hypotheses/` = offene Hypothesen-Bündel
5. `04_extracts/` = getrennte Extraktions-Artefakte
6. `05_mapping/` = Mapping in stabile Zielklassen
7. `06_review/` = review_required-Datensätze
8. `07_reports/` = Zusammenfassungen und Abnahme

## Für Arbeitgeber

Dieses Repo ist nützlich, wenn du sehen willst, wie ich mit Folgendem umgehe:

1. Recovery von unklarem Legacy-Material
2. Trennung zwischen Evidenz und Interpretation
3. append-only Denke und Provenienz-Disziplin
4. vorsichtigen Workflows, die Sicherheit nicht überbehaupten

## Verwandte öffentliche Repos

- [`tof_bridge_planning_method`](https://github.com/IMaugrenI/tof-bridge-planning-method) — Planungs-Baseline nach der Recovery
- [`tof_local_builder`](https://github.com/IMaugrenI/tof_local_builder) — lokaler Builder-Stack
- [`tof_local_knowledge`](https://github.com/IMaugrenI/tof_local_knowledge) — on-prem lokales Wissenssystem
