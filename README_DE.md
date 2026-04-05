# tof-legacy-recovery-workbench

> Die englische Hauptfassung liegt in `README.md`.

Public_safe Recovery_Workbench fuer aelteres gemischtes Material.

Ich nutze dieses Repo, um zu zeigen, wie ich Evidenz trenne, Herkunft sichere und falsche Sicherheit bei Recovery_Arbeit vermeide.

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

## was_dieses_repo_macht

1. es liest Legacy_Input aus `00_input_alt/`
2. es baut append_only JSON Artefakte ueber feste Stufen
3. es erkennt Discord_, Bot_ und Repo_Runtime Signale
4. es trennt gemischte Funde statt sie zu einer einzigen Wahrheit zusammenzuziehen
5. es mappt Ergebnisse in stabile Zielklassen
6. es haelt review_required Faelle sichtbar

## warum_das_wichtig_ist

1. altes Material ist oft gemischt, unvollstaendig oder irrefuehrend
2. Herkunft ist bei Recovery entscheidend
3. Unsicherheit soll sichtbar bleiben
4. Recovery ist nicht dasselbe wie Runtime_Wahrheit
5. Standardlaeufe sollen nicht still Zielcode erzeugen

## pipeline

1. `00_input_alt/` = altes Eingabematerial
2. `01_intake/` = Intake_Datensaetze pro Quelle
3. `02_evidence/` = neutrale Evidenzschicht
4. `03_hypotheses/` = offene Hypothesenbuendel
5. `04_extracts/` = getrennte Extraktionsartefakte
6. `05_mapping/` = Mapping in stabile Zielklassen
7. `06_review/` = review_required Datensaetze
8. `07_reports/` = Zusammenfassungen und Annahme

## fuer_arbeitgeber

Dieses Repo ist nuetzlich, wenn du sehen willst, wie ich mit folgenden Dingen umgehe:

1. Recovery von unklarem Legacy_Material
2. Trennung von Evidenz und Interpretation
3. append_only Denken und Herkunftsdisziplin
4. vorsichtige Workflows ohne ueberzogene Sicherheitsbehauptungen

## verwandte_oeffentliche_repos

- [`tof_bridge_planning_method`](https://github.com/IMaugrenI/tof-bridge-planning-method) — Planungs_Baseline nach der Recovery
- [`tof_local_builder`](https://github.com/IMaugrenI/tof_local_builder) — lokaler Builder_Stack
- [`tof_local_knowledge`](https://github.com/IMaugrenI/tof_local_knowledge) — on_prem lokales Wissenssystem
