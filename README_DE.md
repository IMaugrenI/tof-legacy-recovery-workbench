# tof-legacy-recovery-workbench

> Deutsch ist die Spiegelversion dieses Repositories. Der englische Primärtext liegt in `README.md`.

Öffentlich sichere Recovery-Workbench-Baseline zum Lesen älterer gemischter Materialien, zum Trennen verwertbarer Substanz und zum Mapping auf stabile Zielklassen.

## Kurzüberblick

- liest Altinput aus `00_input_alt/`
- baut append-only JSON-Artefakte über feste Stufen auf
- erkennt Discord-, Bot- und Repo-/Runtime-Signale
- splittet gemischte Funde statt sie zu einer Wahrheit zu verschmelzen
- mappt Ergebnisse auf stabile Zielklassen:
  - `discord`
  - `bot`
  - `repo`
  - `review_required`
- erzeugt standardmäßig **keinen** Zielcode

## Warum dieses Repo existiert

Dieses Repository ist eine öffentliche Baseline für ein Recovery-/Workbench-Muster:

- ältere oder gemischte Quellen einlesen
- Herkunft sichtbar halten
- Evidenz von Interpretation trennen
- Unsicherheit sichtbar lassen
- verwertbare Substanz vorbereiten, ohne sie als aktive Runtime-Wahrheit auszugeben

## Was dieses Repo ist

- eine reduzierte technische Workbench-Baseline
- eine lauffähige Demo-Pipeline
- ein öffentlich sicheres Beispiel für Legacy-Recovery- und Mapping-Disziplin

## Was dieses Repo nicht ist

- nicht der private Arbeitskorpus
- nicht der vollständige interne Recovery-Raum
- keine Runtime-Wahrheit
- keine automatische Code-Generierung
- kein blindes Migrationstool

## Pipeline-Stufen

1. `00_input_alt/` – Altinput
2. `01_intake/` – Intake-Records pro Quelle
3. `02_evidence/` – neutrale Evidenzschicht
4. `03_hypotheses/` – Open-Set-Hypothesenbündel
5. `04_extracts/` – Split-Extraktionsartefakte
6. `05_mapping/` – Mapping auf stabile Zielklassen
7. `06_review/` – Review-pflichtige Records
8. `07_reports/` – Summary, Dubletten, Acceptance

## Schnellstart

### Lokal

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
tof-workbench run
```

### Docker

```bash
docker compose up --build werkbank
```

## Demo-Input

Das Repository enthält nur öffentlich sichere fiktive Beispiele:

- ein Discord-Kanal-Notizbündel
- ein kleines Bot-Modul
- ein compose-artiges Runtime-Fragment
- eine Entrypoint-Datei ohne Endung

## Wichtige Regeln

- Dateien ohne Endung sind First-Class-Input
- alte Hinweise sind nur Hinweise, nicht Wahrheit
- Open-Set-Erkennung erzeugt keine neuen Zielklassen
- Zielklassen bleiben klein und stabil
- der Default-Lauf materialisiert keinen Zielcode

## Verwandte öffentliche Repos

- [`tof_local_builder`](https://github.com/IMaugrenI/tof_local_builder) — lokaler Builder-Stack
- [`tof_local_knowledge`](https://github.com/IMaugrenI/tof_local_knowledge) — on-prem lokales Wissenssystem
- [`tof-bridge-planning-method`](https://github.com/IMaugrenI/tof-bridge-planning-method) — Brückenplanungs-Methodenebene
