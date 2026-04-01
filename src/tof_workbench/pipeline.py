from __future__ import annotations

import asyncio
from pathlib import Path

from .acceptance import run_acceptance
from .duplicates import run_duplicates
from .evidence import run_evidence
from .extractors import run_extractors
from .hypotheses import run_hypotheses
from .intake import run_intake
from .io_utils import write_json
from .mapping import run_mapping


async def run_default_pipeline(repo_root: Path) -> dict:
    intake = await run_intake(repo_root)
    evidence = await run_evidence(repo_root)
    hypotheses = await run_hypotheses(repo_root)
    extracts = await run_extractors(repo_root)
    mapping = await run_mapping(repo_root)
    duplicates = run_duplicates(repo_root)
    acceptance = run_acceptance(repo_root)
    summary = {
        'intake': len(intake),
        'evidence': len(evidence),
        'hypotheses': len(hypotheses),
        'extracts': len(extracts),
        'mapping': len(mapping),
        'exact_duplicates': len(duplicates.get('exact_duplicates', [])),
        'near_duplicates': len(duplicates.get('near_duplicates', [])),
        'coverage_ratio': acceptance.get('coverage_ratio'),
    }
    write_json(repo_root / '07_reports' / 'run_summary.json', summary)
    return summary
