# tof-legacy-recovery-workbench

> Die englische Hauptfassung liegt in `README.md`.

Public-safe Recovery-Werkbank für älteres, gemischtes Material.

Ich nutze dieses Repo, um zu zeigen, wie ich Evidenz trenne, Herkunft bewahre und falsche Sicherheit während der Recovery-Arbeit vermeide.

## Warum dieses Repo öffentlich ist

Ich habe dieses Repo öffentlich gemacht, weil Recovery-Arbeit einen wichtigen Teil davon zeigt, wie ich baue.

Ich will altes Material nicht glätten oder schönreden. Ich will es sorgfältig lesen, sauber trennen, Herkunft erhalten und Unsicherheit sichtbar lassen.

Recovery ist nicht dasselbe wie Runtime-Wahrheit. Dieses Repo existiert, um zu zeigen, dass ich methodisch arbeite, statt alles zu vermischen.

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

1. liest Altmaterial aus `00_input_alt/`
2. baut append-only JSON-Artefakte über feste Stufen hinweg
3. erkennt Discord-, Bot- und Repo-Runtime-Signale
4. trennt gemischte Funde, statt sie zu einer Wahrheit zusammenzuziehen
5. ordnet Ergebnisse stabilen Zielklassen zu
6. hält review_required-Fälle sichtbar

## Warum das wichtig ist

1. altes Material ist oft gemischt, unvollständig oder irreführend
2. Herkunft ist während Recovery-Arbeit wichtig
3. Unsicherheit muss sichtbar bleiben
4. Recovery ist nicht dasselbe wie Runtime-Wahrheit
5. Standardläufe dürfen nicht stillschweigend Zielcode erzeugen

## Pipeline

1. `00_input_alt/` = Altmaterial
2. `01_intake/` = Intake-Datensätze pro Quelle
3. `02_evidence/` = neutrale Evidenzebene
4. `03_hypotheses/` = offene Hypothesenbündel
5. `04_extracts/` = getrennte Extraktionsartefakte
6. `05_mapping/` = Zuordnung zu stabilen Zielklassen
7. `06_review/` = review_required-Datensätze
8. `07_reports/` = Zusammenfassungen und Annahme

## Für Arbeitgeber

Dieses Repo ist nützlich, wenn du sehen willst, wie ich mit Folgendem umgehe:

1. Recovery von unklarem Altmaterial
2. Trennung von Evidenz und Interpretation
3. append-only Denken und Herkunftsdisziplin
4. vorsichtigen Workflows, die Sicherheit nicht überbehaupten

## Verwandte öffentliche Repos

- [`tof_bridge_planning_method`](https://github.com/IMaugrenI/tof-bridge-planning-method) — Planungsbasis nach Recovery
- [`tof_local_builder`](https://github.com/IMaugrenI/tof_local_builder) — lokaler Builder-Stack
- [`tof_local_knowledge`](https://github.com/IMaugrenI/tof_local_knowledge) — on-prem lokales Wissenssystem
